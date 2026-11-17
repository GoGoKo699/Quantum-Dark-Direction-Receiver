# Parity and the conjugate hole

Two independently mixed specimens can reveal a pure description of their occupied plane. The antisymmetric component of a rank-two pair is the wedge of its occupied vectors; in dimension three, that wedge identifies the missing ray through a conjugate Hodge map. The measurement architecture is inherited from collective symmetry readout and Keyl estimation; [related work](../references/RELATED_WORK.md) separates it from the finite-budget result here.

## Registers and outcome labels

Let $`S`$ exchange the two qutrits and set $`P_\pm=(I\pm S)/2`$. Use normalized wedge basis $`(e_0\wedge e_1,e_0\wedge e_2,e_1\wedge e_2)`$. The conjugate identification is

```math
g(f)=(\overline f_2,-\overline f_1,\overline f_0).
```

If the pair source is $`\rho_f^{\otimes2}`$, the antisymmetric branch has probability $`1/4`$ and normalized state $`P_{g(f)}`$. The symmetric branch has probability $`3/4`$. The map preserves ray overlaps. We label an antisymmetric effect by the **dark-space ray** $`\psi`$, with physical effect on $`g(\psi)`$. Using the same coordinate vector literally in the wedge register would change that label and the finite MUB overlap calculation.

For normalized positive weights $`w_\ell`$ and rays $`\psi_\ell`$ forming a projective 2-design, define

```math
E_\ell^+=6w_\ell|\psi_\ell\psi_\ell\rangle
 \!\langle\psi_\ell\psi_\ell|,
\qquad
E_\ell^-=3w_\ell P_{g(\psi_\ell)}.
```

The design identities give $`\sum_\ell E_\ell^+=P_+`$ and $`\sum_\ell E_\ell^-=P_-`$, so this is a POVM on the full nine-dimensional pair space. Every effect is independent of the unknown ray.

## The 24-outcome small-budget receiver

Take the twelve rays in the four qutrit mutually unbiased bases, with $`w_\ell=1/12`$. With $`\omega=e^{2\pi i/3}`$, these are the three computational rays and

```math
\psi_{AB}=\frac1{\sqrt3}\sum_{j=0}^2
 \omega^{Aj^2+Bj}|j\rangle,
\qquad A,B\in\{0,1,2\}.
```

The symmetric effects have coefficient $`1/2`$ and the wedge effects coefficient $`1/4`$. The remaining third specimen is measured by $`F_\ell=P_{\psi_\ell}/4`$. This gives 24 pair outcomes and 12 single outcomes. A common known laboratory rotation of all effects and of the reported ray supplies the covariant comparison. [Finite budgets](finite-budget.md) gives the estimator and exact score; [implementation](implementation.md) replaces the continuous setting by finite randomness with a quantified error.

This unregularized 24-outcome receiver differs from the positive-probability regularized construction in Quantum Off the Wall. Finite direct risk calculations do not require its tiny probability floor or an asymptotic score estimator.

## A fixed 450-outcome moment receiver

The larger-budget construction uses an explicit weighted projective 4-design. A Haar ray can be represented by

```math
\psi=\left(\sqrt u,\sqrt{(1-u)v}\,e^{i\phi_1},
 \sqrt{(1-u)(1-v)}\,e^{i\phi_2}\right),
```

where $`u`$ has density $`2(1-u)`$ on $`[0,1]`$, $`v`$ is uniform, and the phases are independent uniform angles. Replace $`u`$ by three-point Gauss–Jacobi quadrature for that density, $`v`$ by three-point Gauss–Legendre quadrature, and each phase by the five roots of unity. This gives $`3\cdot3\cdot5\cdot5=225`$ rays with positive normalized algebraic weights.

For projective moments through degree four, each phase exponent difference lies between $`-4`$ and $`4`$. The five-point phase sums therefore eliminate precisely the same off-diagonal monomials as Haar averaging. Surviving monomials have degree at most four in each quadrature variable; three-point Gaussian quadrature is exact through degree five. This proves the 4-design identity. Degree two proves measurement completeness; degree four supplies the exact matrix variance.

Use both branches of the displayed POVM, giving 450 fixed rank-one effects. For each complete pair record, form

```math
Z=\begin{cases}
2I-5P_{\psi_\ell},&+,\\
4P_{\psi_\ell}-I,&-.
\end{cases}
```

The estimate after $`K`$ pairs is the leading eigenray of $`K^{-1}\sum Z`$, with a deterministic tie convention. This is the two-copy debiased Keyl matrix estimator specialized to $`P_f=I-2\rho_f`$; its ideal coefficient $`6.6`$ is inherited, rather than a new optimization result.

The accumulated data are a $`3\times3`$ Hermitian matrix and outcome/branch counts. Processing is $`O(K)`$ in this fixed dimension. One stored qutrit and constant-dimensional ancillary control suffice under the explicit dilation model. Neither the existence of that dilation nor its simulation supplies the finite superiority theorem; the relevant risk proofs are separate.
