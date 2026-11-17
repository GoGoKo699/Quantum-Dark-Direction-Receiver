"""Reproducible finite-design moments and bounded-memory receiver checks.

The receiver architecture/debiased estimator are inherited from PSW arXiv:2510.07788.
The finite comparison concerns first-copy depolarizing memory and global ray risk.
"""
import json, math
from pathlib import Path
import numpy as np
from scipy.special import roots_jacobi, roots_legendre

HERE=Path(__file__).resolve().parent
SEED=2026111701

def design():
    # u~Beta(1,2), v~Uniform(0,1); two independent five-point phases.
    xu,wu=roots_jacobi(3,1,0); xv,wv=roots_legendre(3)
    rays=[]; weights=[]
    for u,a in zip((xu+1)/2,wu/2):
        for v,b in zip((xv+1)/2,wv/2):
            for j in range(5):
                for k in range(5):
                    rays.append([np.sqrt(u),np.sqrt((1-u)*v)*np.exp(2j*np.pi*j/5),
                                 np.sqrt((1-u)*(1-v))*np.exp(2j*np.pi*k/5)])
                    weights.append(a*b/25)
    rays=np.array(rays); weights=np.array(weights)
    Q=np.einsum('ni,nj->nij',rays,rays.conj())
    return rays,weights,Q

def exact_checks(rays,w,Q):
    errors=[]
    import itertools
    for t in range(1,5):
        for a in itertools.product(range(3),repeat=t):
            occa=np.bincount(a,minlength=3)
            va=np.prod(rays[:,a],axis=1)
            for b in itertools.product(range(3),repeat=t):
                occb=np.bincount(b,minlength=3)
                actual=np.sum(w*va*np.prod(rays[:,b].conj(),axis=1))
                target=0 if np.any(occa!=occb) else 2*math.prod(math.factorial(int(n)) for n in occa)/math.factorial(t+2)
                errors.append(abs(actual-target))
    return {'ray_count':len(w),'outcome_count':2*len(w),'weight_sum':float(w.sum()),
            'max_projective_moment_error_degree_1_to_4':float(max(errors))}

def main():
    rng=np.random.default_rng(SEED);rays,w,Q=design()
    output={'seed':SEED,'design':exact_checks(rays,w,Q),'moment_checks':[], 'monte_carlo':[]}
    # Independent Born-rule check in the full physical 9-dimensional pair space.
    W=np.zeros((9,3),complex)
    for k,(i,j) in enumerate([(0,1),(0,2),(1,2)]):
        W[3*i+j,k]=1/np.sqrt(2);W[3*j+i,k]=-1/np.sqrt(2)
    sk=np.einsum('ni,nj->nij',rays,rays).reshape(-1,9)
    g=np.column_stack((rays[:,2].conj(),-rays[:,1].conj(),rays[:,0].conj()))
    ak=g@W.T
    Es=6*w[:,None,None]*np.einsum('ni,nj->nij',sk,sk.conj())
    Ea=3*w[:,None,None]*np.einsum('ni,nj->nij',ak,ak.conj())
    effects=np.concatenate([Es,Ea])
    fb=np.array([1,1j,.3]);fb/=np.linalg.norm(fb)
    Pb=np.outer(fb,fb.conj());rho=(np.eye(3)-Pb)/2;u=np.abs(rays.conj()@fb)**2
    born_errors=[]
    for nu in [0,.8,.9,1.]:
        tau=np.kron(nu*rho+(1-nu)*np.eye(3)/3,rho)
        direct=np.einsum('nij,ji->n',effects,tau).real
        formula=np.r_[w*((3*nu/2)*(1-u)**2+(1-nu)*(1-u)),
                      w*((1-nu)/4+(2*nu+1)*u/4)]
        born_errors.append(float(np.max(np.abs(direct-formula))))
    output['full_pair_born_checks']={'completeness_error':float(np.linalg.norm(effects.sum(axis=0)-np.eye(9))),
       'minimum_effect_eigenvalue':float(np.linalg.eigvalsh(effects).min()),
       'maximum_probability_formula_error':max(born_errors)}
    Zs=2*np.eye(3)[None,:,:]-5*Q
    Za=4*Q-np.eye(3)[None,:,:]
    Z=np.concatenate([Zs,Za])
    # Check full matrix moments at random orientations.
    for nu in [0,.8,.9,1.]:
        for _ in range(3):
            f=rng.normal(size=3)+1j*rng.normal(size=3);f/=np.linalg.norm(f)
            P=np.outer(f,f.conj());u=np.abs(rays.conj()@f)**2
            ps=w*((3*nu/2)*(1-u)**2+(1-nu)*(1-u))
            pa=w*((1-nu)/4+(2*nu+1)*u/4)
            p=np.r_[ps,pa];M=np.einsum('n,nij->ij',p,Z)
            target=(1+nu)/2*P+(1-nu)/6*np.eye(3)
            X=Z-target
            var=np.einsum('n,nij,njk->ik',p,X,X)
            vartarget=(182+8*nu-nu*nu)/36*np.eye(3)-(8+6*nu+nu*nu)/12*P
            V=sum(p[i]*(np.vdot(Z[i]@f,Z[i]@f).real-abs(np.vdot(f,Z[i]@f))**2) for i in range(len(p)))
            output['moment_checks'].append({'nu':nu,'prob_sum_error':float(abs(p.sum()-1)),
                 'mean_error':float(np.linalg.norm(M-target)), 'variance_error':float(np.linalg.norm(var-vartarget)),
                 'tangent_variance_error':float(abs(V-(103-4*nu)/30))})
    # Selected one-copy comparison only: finite-design covariant moment estimator.
    # This is NOT the optimal adaptive one-copy comparator used by the theorem.
    for N in [50,100,200,1000,5000]:
        for nu in [1.,.9,.8]:
            pairloss=[];singleloss=[]
            for _ in range(10):
                f=rng.normal(size=3)+1j*rng.normal(size=3);f/=np.linalg.norm(f)
                u=np.abs(rays.conj()@f)**2
                ps=w*((3*nu/2)*(1-u)**2+(1-nu)*(1-u))
                pa=w*((1-nu)/4+(2*nu+1)*u/4)
                p=np.r_[ps,pa];p/=p.sum()
                counts=rng.multinomial(N//2,p,size=100)
                mat=np.einsum('rn,nij->rij',counts,Z)/(N//2)
                _,eig=np.linalg.eigh(mat);fh=eig[:,:,-1]
                pairloss.extend(1-np.abs(fh.conj()@f)**2)
                q=1.5*w*(1-u);q/=q.sum()
                count1=rng.multinomial(N,q,size=100)
                mat1=np.einsum('rn,nij->rij',count1,Q)/N
                _,eig1=np.linalg.eigh(mat1);fh1=eig1[:,:,0]
                singleloss.extend(1-np.abs(fh1.conj()@f)**2)
            pairloss=np.array(pairloss);singleloss=np.array(singleloss)
            output['monte_carlo'].append({'specimens':N,'nu':nu,'trials':len(pairloss),
               'mean_pair_infidelity':float(pairloss.mean()),'pair_standard_error':float(pairloss.std(ddof=1)/np.sqrt(len(pairloss))),
               'mean_selected_single_infidelity':float(singleloss.mean()),
               'single_standard_error':float(singleloss.std(ddof=1)/np.sqrt(len(singleloss))),
               'scaled_pair':float(N*pairloss.mean()),'scaled_selected_single':float(N*singleloss.mean())})
    finite=[]
    for K,nu,t in [(100000,1,.043),(200000,.95,.031),(1000000,.9,.015),(10000000,.85,.0051)]:
        b=(1+nu)/2;V=(103-4*nu)/30
        main=V/(K*(b-2*t)**2);tail=6*math.exp(-K*t*t/(10.5+8*t/3))
        N=2*K;lower=16/(N+24+math.sqrt(N*(N+16)))
        finite.append({'pairs':K,'specimens':N,'nu':nu,'t':t,'main_upper':main,
           'bad_event_upper':tail,'total_upper':main+tail,'all_adaptive_one_copy_lower':lower,
           'strict_separation':main+tail<lower})
    output['finite_bound_evaluations']=finite
    assert output['design']['max_projective_moment_error_degree_1_to_4'] < 1e-12
    assert output['full_pair_born_checks']['completeness_error'] < 1e-11
    assert output['full_pair_born_checks']['minimum_effect_eigenvalue'] > -1e-12
    assert output['full_pair_born_checks']['maximum_probability_formula_error'] < 1e-12
    for row in output['moment_checks']:
        assert row['prob_sum_error'] < 1e-12
        assert row['mean_error'] < 1e-11
        assert row['variance_error'] < 1e-10
        assert row['tangent_variance_error'] < 1e-11
    assert all(row['strict_separation'] for row in finite)
    # Results are emitted to stdout; callers may capture them outside the source tree.
    print(json.dumps(output,indent=2))

if __name__=='__main__': main()
