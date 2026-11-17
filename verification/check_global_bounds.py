"""Check intrinsic information normalization and exact noisy-channel identities.

Finite numerical cases corroborate the analytical all-protocol bounds; they
do not enumerate adaptive POVMs or establish a no-go theorem by sampling.
"""
import json
from fractions import Fraction as F
import numpy as np
from check_implementation import mub_rays


def projector(v):
    return np.outer(v, v.conj())


def main():
    rng = np.random.default_rng(2026111704)
    fisher_errors = []
    coarse_traces = []
    for _ in range(12):
        a = rng.normal(size=(3, 15)) + 1j*rng.normal(size=(3, 15))
        values, vectors = np.linalg.eigh(a@a.conj().T)
        frame = (vectors@np.diag(values**-.5)@vectors.conj().T)@a
        effects = np.einsum('ik,jk->kij', frame, frame.conj())
        f = rng.normal(size=3)+1j*rng.normal(size=3)
        f /= np.linalg.norm(f)
        p = projector(f)
        _, basis = np.linalg.eigh(np.eye(3)-p)
        tangent = [basis[:, 1], 1j*basis[:, 1], basis[:, 2], 1j*basis[:, 2]]
        rho = (np.eye(3)-p)/2
        probs = np.einsum('kij,ji->k', effects, rho).real
        deriv = np.array([np.einsum('kij,ji->k', effects,
                         -(np.outer(d, f.conj())+np.outer(f, d.conj()))/2).real
                          for d in tangent])
        trace = np.sum(deriv**2/probs)
        fisher_errors.append(abs(trace-2))
        cp = probs.reshape(5,3).sum(axis=1)
        cd = deriv.reshape(4,5,3).sum(axis=2)
        coarse_traces.append(float(np.sum(cd**2/cp)))
    # Exact quadratic/root normalization in the finite global lower bound.
    for n in (0,1,2,3,100,3_000_000):
        # At r=8/(n+16), the lower quadratic is nonnegative; this is the
        # conservative rational lower used in the paid-calibration certificate.
        r = F(8,n+16)
        polynomial = (n+18)*r*r-(n+24)*r+8
        assert polynomial >= 0
    rays = mub_rays()
    effects1 = np.array([projector(v)/4 for v in rays])
    eb_errors = []
    for nu in (0,.1,.25):
        prep = np.array([4*nu*projector(v)+(1-4*nu)*np.eye(3)/3 for v in rays])
        assert np.linalg.eigvalsh(prep).min() >= -1e-14
        for _ in range(4):
            a = rng.normal(size=(3,3))+1j*rng.normal(size=(3,3))
            rho = a@a.conj().T;rho /= np.trace(rho)
            probs = np.einsum('kij,ji->k', effects1, rho).real
            direct = np.einsum('k,kij->ij', probs, prep)
            eb_errors.append(float(np.linalg.norm(direct-(nu*rho+(1-nu)*np.eye(3)/3))))
    wedge = np.zeros((9,3),complex)
    for k,(i,j) in enumerate(((0,1),(0,2),(1,2))):
        wedge[3*i+j,k]=1/np.sqrt(2);wedge[3*j+i,k]=-1/np.sqrt(2)
    g = np.column_stack((rays[:,2].conj(),-rays[:,1].conj(),rays[:,0].conj()))
    anti = g@wedge.T
    sym = np.einsum('ni,nj->nij',rays,rays).reshape(12,9)
    pair_effects = np.concatenate((np.array([projector(v)/2 for v in sym]),
                                   np.array([projector(v)/4 for v in anti])))
    swap_errors=[]
    for _ in range(8):
        f=rng.normal(size=3)+1j*rng.normal(size=3);f/=np.linalg.norm(f)
        h=rng.normal(size=3)+1j*rng.normal(size=3);h/=np.linalg.norm(h)
        r1=(np.eye(3)-projector(f))/2;r2=(np.eye(3)-projector(h))/2
        v=np.einsum('kij,ji->k',pair_effects,np.kron(r1,r2)-np.kron(r2,r1))
        swap_errors.append(float(np.max(abs(v))))
    assert max(fisher_errors)<1e-12
    assert max(coarse_traces)<=2+1e-12
    assert max(eb_errors)<1e-12
    assert max(swap_errors)<1e-12
    print(json.dumps({'status':'passed','seed':2026111704,
        'maximum_intrinsic_rank_one_fisher_trace_error':max(fisher_errors),
        'maximum_coarse_grained_fisher_trace':max(coarse_traces),
        'maximum_entanglement_breaking_identity_error':max(eb_errors),
        'maximum_coherent_exchange_probability_error':max(swap_errors),
        'scope':'Selected matrix identities; general bounds are proved analytically.'},indent=2))


if __name__ == '__main__':
    main()
