"""Numerical checks of the finite implementation identities and error budget.

The Gaussian coupling, conditioning probability, and score-error bounds are
proved in science/implementation.md. These finite numerical checks do not
certify a laboratory control channel or replace that proof.
"""
import json
import math
import random
import numpy as np
import mpmath as mp
from scipy.linalg import expm

SEED = 2026111703


def mub_rays():
    omega = np.exp(2j * np.pi / 3)
    vectors = [v.astype(complex) for v in np.eye(3)]
    for a in range(3):
        for b in range(3):
            vectors.append(np.array([omega ** (a*j*j+b*j) for j in range(3)]) / np.sqrt(3))
    return np.asarray(vectors)


def complete_isometry(j, dimension):
    """Complete the stated first columns, rather than change them by QR phases."""
    columns = [v.copy() for v in np.pad(j, ((0, dimension-j.shape[0]), (0, 0))).T]
    for k in range(dimension):
        v = np.eye(dimension, dtype=complex)[:, k]
        for _ in range(2):
            for col in columns:
                v -= col * np.vdot(col, v)
        norm = np.linalg.norm(v)
        if norm > 1e-10:
            columns.append(v/norm)
        if len(columns) == dimension:
            break
    assert len(columns) == dimension
    return np.column_stack(columns)


def direct_isometry_dilation(j, dimension):
    """Column elimination supplies a finite selective-transition gate program."""
    d = j.shape[1]
    a = np.pad(j, ((0,dimension-j.shape[0]),(0,0))).copy()
    rotations = []
    for col in range(d):
        for row in range(dimension-1,col,-1):
            aa,bb = a[col,col],a[row,col]
            if abs(bb) < 1e-14:
                continue
            r = math.hypot(abs(aa),abs(bb))
            g = np.array([[aa.conjugate(),bb.conjugate()],[-bb,aa]])/r
            a[[col,row],:] = g@a[[col,row],:]
            rotations.append((col,row,g))
    diagonal = np.ones(dimension,complex)
    diagonal[:d] = np.diag(a[:d,:])
    u = np.diag(diagonal)
    for first,second,g in reversed(rotations):
        u[[first,second],:] = g.conj().T@u[[first,second],:]
    target = np.pad(j, ((0,dimension-j.shape[0]),(0,0)))
    return {'mixing_blocks':len(rotations),'phase_blocks':d,
            'mixing_block_upper_bound':d*dimension-d*(d+1)//2,
            'first_columns_error':float(np.linalg.norm(u[:,:d]-target)),
            'unitarity_error':float(np.linalg.norm(u.conj().T@u-np.eye(dimension)))}


def givens_reconstruction_error(target):
    """Construct a finite sequence of selective two-level mixing blocks."""
    a = target.copy(); rotations = []; n = len(a)
    for col in range(n-1):
        for row in range(n-1, col, -1):
            x, y = a[row-1, col], a[row, col]
            r = math.hypot(abs(x), abs(y))
            if r < 1e-14:
                continue
            g = np.array([[x.conjugate()/r, y.conjugate()/r], [-y/r, x/r]])
            a[[row-1, row], :] = g @ a[[row-1, row], :]
            rotations.append((row-1, row, g))
    diagonal = np.diag(np.diag(a))
    reconstructed = diagonal.copy()
    for i, j, g in reversed(rotations):
        reconstructed[[i, j], :] = g.conj().T @ reconstructed[[i, j], :]
    return {'mixing_blocks': len(rotations), 'diagonal_phases': n,
            'upper_triangle_residual': float(np.linalg.norm(a-diagonal)),
            'reconstruction_error': float(np.linalg.norm(reconstructed-target))}


def polar(a):
    u, _, vh = np.linalg.svd(a)
    return u @ vh


def finite_gaussian_coupling_checks(t, small_a, epsilon, bits, rng):
    gamma = small_a**3/(18*t*t); h = gamma*epsilon/8
    phi = math.exp(-(t+1)**2/2)/math.sqrt(2*math.pi)
    assert 2.0**(-bits) <= h*phi/2
    # More than enough accuracy for 128-bit inverse-CDF arguments and this h.
    # This validates examples; certified interval arithmetic is required by the
    # abstract implementation if its numerical error is used in a proof.
    mp.mp.dps = 100
    grid_bits = math.ceil(math.log2(4/h))
    errors = []; polar_errors = []; condition_numbers = []
    for _ in range(8):
        exact = []; finite = []
        for _ in range(18):
            draw = rng.getrandbits(256)
            x = (mp.mpf(draw)+mp.mpf('0.5')) / mp.mpf(2)**256
            r = draw >> (256-bits)
            midpoint = (mp.mpf(r)+mp.mpf('0.5')) / mp.mpf(2)**bits
            q = mp.sqrt(2)*mp.erfinv(2*midpoint-1)
            q_grid = mp.nint(q*mp.mpf(2)**grid_bits) / mp.mpf(2)**grid_bits
            exact.append(float(mp.sqrt(2)*mp.erfinv(2*x-1)))
            finite.append(float(q_grid))
        g = (np.array(exact)[::2] + 1j*np.array(exact)[1::2]).reshape(3,3)
        hh = (np.array(finite)[::2] + 1j*np.array(finite)[1::2]).reshape(3,3)
        errors.append(float(np.linalg.norm(g-hh,2)))
        polar_errors.append(float(np.linalg.norm(polar(g)-polar(hh),2)))
        condition_numbers.append(float(np.linalg.svd(hh,compute_uv=False)[-1]))
    return {'bits_per_real_coordinate': bits, 'fair_bits_total':18*bits,
            'gamma':gamma, 'quantile_grid_h':h, 'dyadic_fractional_bits':grid_bits,
            'inverse_cdf_bit_condition_ratio':2.0**(-bits)/(h*phi/2),
            'coordinate_coupling_matrix_bound':3*h/math.sqrt(2),
            'maximum_sampled_matrix_coupling_error':max(errors),
            'maximum_sampled_polar_coupling_error':max(polar_errors),
            'minimum_sampled_singular_value':min(condition_numbers),
            'bad_setting_probability_bound':36*math.exp(-t*t/2)+1.5*small_a*small_a}


def posterior_outputs(q):
    out = np.empty((2,12,12,3,3),complex)
    scores = []
    for branch in range(2):
        total = 0
        for i,a in enumerate(q):
            for j,b in enumerate(q):
                c = np.trace(a@b).real
                if branch == 0:
                    k = ((52+8*c)*np.eye(3)-(28+4*c)*a-20*b+8*(a@b+b@a))/160
                else:
                    k = 3*((4-c)*np.eye(3)+4*a-b-a@b-b@a)/160
                vals, vecs = np.linalg.eigh(k)
                v = vecs[:,-1]; out[branch,i,j] = np.outer(v,v.conj())
                total += vals[-1]/144
        scores.append(total)
    return out, scores


def fidelity(f, rays, outputs):
    u = np.abs(rays.conj()@f)**2
    pair = np.stack(((1-u)**2/8, u/16))
    single = (1-u)/8
    scores = np.einsum('i,baqij,j->baq',f.conj(),outputs,f).real
    return float(np.einsum('ba,q,baq->',pair,single,scores))


def main():
    rng = np.random.default_rng(SEED); integer_rng = random.Random(SEED)
    rays = mub_rays(); q = np.einsum('ni,nj->nij',rays,rays.conj())
    wedge = np.zeros((9,3),complex)
    for k,(i,j) in enumerate(((0,1),(0,2),(1,2))):
        wedge[3*i+j,k] = 1/np.sqrt(2); wedge[3*j+i,k] = -1/np.sqrt(2)
    sym = np.einsum('ni,nj->nij',rays,rays).reshape(12,9)
    g = np.column_stack((rays[:,2].conj(),-rays[:,1].conj(),rays[:,0].conj()))
    anti = g@wedge.T
    jpair = np.concatenate((sym.conj()/np.sqrt(2),anti.conj()/2))
    jsingle = rays.conj()/2
    upair = complete_isometry(jpair,36); usingle = complete_isometry(jsingle,12)
    outputs, branch_scores = posterior_outputs(q)
    target_fidelity = 41/120+(127+9*math.sqrt(17))/1280
    gap = 53735011/1e8-(1-target_fidelity)
    score_lipschitz = []
    for _ in range(12):
        f = rng.normal(size=3)+1j*rng.normal(size=3); f/=np.linalg.norm(f)
        u = polar(rng.normal(size=(3,3))+1j*rng.normal(size=(3,3)))
        a = rng.normal(size=(3,3))+1j*rng.normal(size=(3,3)); a=(a+a.conj().T)/2
        v = u@expm(1j*1e-5*a)
        change = abs(fidelity(u.conj().T@f,rays,outputs)-fidelity(v.conj().T@f,rays,outputs))
        score_lipschitz.append(change/(8*np.linalg.norm(u-v,2)))
    finite = finite_gaussian_coupling_checks(8,.01,1e-4,128,integer_rng)
    extra = 8e-4+finite['bad_setting_probability_bound']+3e-4
    report = {'seed':SEED,
        'pair_outcomes':24,'single_outcomes':12,'pair_dilation_dimension':36,'single_dilation_dimension':12,
        'pair_isometry_error':float(np.linalg.norm(jpair.conj().T@jpair-np.eye(9))),
        'single_isometry_error':float(np.linalg.norm(jsingle.conj().T@jsingle-np.eye(3))),
        'pair_unitarity_error':float(np.linalg.norm(upair.conj().T@upair-np.eye(36))),
        'single_unitarity_error':float(np.linalg.norm(usingle.conj().T@usingle-np.eye(12))),
        'pair_first_columns_error':float(np.linalg.norm(upair[:,:9]-np.pad(jpair,((0,12),(0,0))))),
        'single_first_columns_error':float(np.linalg.norm(usingle[:,:3]-jsingle)),
        'pair_givens':givens_reconstruction_error(upair),
        'single_givens':givens_reconstruction_error(usingle),
        'direct_pair_isometry_compilation':direct_isometry_dilation(jpair,36),
        'direct_single_isometry_compilation':direct_isometry_dilation(jsingle,12),
        'posterior_branch_fidelities':branch_scores,
        'finite_MUB_fidelity':target_fidelity,
        'posterior_fidelity_formula_error':abs(sum(branch_scores)-target_fidelity),
        'ideal_risk_margin':gap,
        'maximum_sampled_score_change_over_8norm_bound':max(score_lipschitz),
        'finite_randomization':finite,
        'total_implementation_added_risk_bound':extra,
        'remaining_certified_risk_margin':gap-extra,
        'scope':'Finite numeric identity checks; probability and worst-case bounds proved analytically; no hardware calibration certification.'}
    assert report['pair_isometry_error'] < 1e-12
    assert report['single_isometry_error'] < 1e-12
    assert report['pair_unitarity_error'] < 1e-11
    assert report['single_unitarity_error'] < 1e-11
    for key in ('direct_pair_isometry_compilation','direct_single_isometry_compilation'):
        assert report[key]['first_columns_error'] < 1e-11
        assert report[key]['unitarity_error'] < 1e-11
        assert report[key]['mixing_blocks'] <= report[key]['mixing_block_upper_bound']
    assert report['posterior_fidelity_formula_error'] < 1e-12
    assert report['remaining_certified_risk_margin'] > 0
    assert report['maximum_sampled_score_change_over_8norm_bound'] < 1
    print(json.dumps(report,indent=2))


if __name__ == '__main__':
    main()
