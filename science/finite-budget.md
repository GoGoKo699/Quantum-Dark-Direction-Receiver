# A finite separation at three specimens

For the exact qutrit family and dark-ray loss in [the model](model.md), two specimens give **no advantage even to an unrestricted collective receiver**. Three specimens suffice: an explicit pair measurement followed by one single-copy measurement beats every adaptive one-copy strategy.

Write

```math
R_{\mathcal C}^{*}(N)=
\inf_{\mathsf P\in\mathcal C}
\sup_{f\in\mathbb{CP}^{2}}
\mathbb E_f[1-\operatorname{tr}(\widehat P P_f)],
\qquad
\rho_f=\frac{I-P_f}{2}.
```

The one-copy class permits arbitrary POVMs, private randomness, classical adaptation, biased estimators, and processing of the complete record. It retains no coherent system carrying information from one specimen to the next. Every preparation attempt counts. The pair strategy consumes exactly three independent specimens and has no localization pilot.

## The finite statement

Let

```math
F_{\mathrm{MUB}}=
\frac{41}{120}+\frac{127+9\sqrt{17}}{1280}.
```

Then

```math
\boxed{
R_{\mathrm{collective}}^{*}(2)
=R_{\mathrm{one}}^{*}(2)=\frac{23}{40},
}
```

whereas at three specimens,

```math
\boxed{
R_{\mathrm{pair+single}}^{*}(3)
\le 1-F_{\mathrm{MUB}}
<
1-\frac{46264989}{100000000}
\le R_{\mathrm{one}}^{*}(3).
}
```

The displayed receiver has worst-case infidelity about $0.53012400$, while every adaptive one-copy receiver has worst-case infidelity at least $0.53735011$. The certified improvement exceeds $0.007226$. A continuous covariant version has the slightly stronger exact risk $1907/3600$.

These are finite worst-case statements. The lower bound does not identify the optimal one-copy risk at three specimens, and neither receiver is claimed to be optimal among pair strategies. The two-specimen equality and three-specimen separation identify the first total budget at which pair access can improve this task; at budgets zero and one the measurement classes coincide.

The measurement architecture is inherited from covariant highest-weight/Keyl measurement and coherent two-copy readout; see [Pelecanos–Spilecki–Wright](https://arxiv.org/abs/2510.07788) and [Zhu–Hayashi](https://arxiv.org/abs/1709.06112). The contribution here is the global finite comparison and its certificate.

## 1. Exact equality at two specimens

Let Haar ray measure have total mass one and fix a guessed ray $H$. Define

```math
B_H^{(2)}
=\int \rho_f^{\otimes2}\operatorname{tr}(H P_f)\,df.
```

By covariance take $H=|0\rangle\langle0|$. With $P_\pm$ the symmetric and antisymmetric pair projectors, its eigenvalues are:

| Pair sector | Subspace | Dimension | Eigenvalue |
|---|---|---:|---:|
| Symmetric | $\lvert00\rangle$ | 1 | $1/40$ |
| Symmetric | $(\lvert0i\rangle+\lvert i0\rangle)/\sqrt2$, $i=1,2$ | 2 | $3/80$ |
| Symmetric | $\operatorname{Sym}^2\operatorname{span}(\lvert1\rangle,\lvert2\rangle)$ | 3 | $1/20$ |
| Antisymmetric | $(\lvert0i\rangle-\lvert i0\rangle)/\sqrt2$, $i=1,2$ | 2 | $1/48$ |
| Antisymmetric | $\lvert1\rangle\wedge\lvert2\rangle$ | 1 | $1/24$ |

Consequently, for every $H$,

```math
B_H^{(2)}
\preceq \frac{P_+}{20}+\frac{P_-}{24}.
```

For any collective POVM $E_y$ and any output $H_y$, its Haar mean fidelity is at most

```math
\sum_y\operatorname{tr}(E_y B_{H_y}^{(2)})
\le \frac{\operatorname{tr}P_+}{20}
+\frac{\operatorname{tr}P_-}{24}
=\frac{17}{40}.
```

Thus every collective strategy has worst-case infidelity at least $23/40$.

A one-copy strategy attains the bound. Measure rank-one effects $w_A A$ and $w_B B$, with the second measurement allowed to depend on the first record. Put $c=\operatorname{tr}(AB)$. Before the likelihood factor $w_Aw_B/4$, the posterior ray matrix is

```math
K_{AB}^{(2)}
=\int P_f(1-\operatorname{tr}A P_f)(1-\operatorname{tr}B P_f)\,df
=\frac{(11+c)I-4(A+B)+AB+BA}{60}.
```

Its largest eigenvalue is $(11+c)/60$, attained by a ray perpendicular to $\operatorname{span}(A,B)$. Indeed, $AB+BA\preceq A+B$, so the remaining correction is negative semidefinite.

Completeness gives $\sum_Bw_B=3$, $\sum_Bw_Bc=1$ for each first record, and $\sum_Aw_A=3$. The achieved Haar mean fidelity is

```math
\frac14\frac{3(11\cdot3+1)}{60}=\frac{17}{40}.
```

One concrete choice measures the same orthonormal basis on both specimens and returns a ray perpendicular to both outcomes, with any fixed perpendicular choice when the outcomes coincide. Conjugating the entire measurement and output rule by one known independent Haar laboratory unitary makes the risk constant over $f$, preserving this mean. This proves the minimax equality.

## 2. A three-specimen attaining strategy

First consider a continuous covariant pair readout. Its complete record contains the SWAP branch $s$ or $a$ and a ray $A$. The antisymmetric output is mapped back to dark-ray space by the conjugate Hodge identification. Relative to normalized Haar ray measure,

```math
h_s(u)=\frac32(1-u)^2,\qquad
h_a(u)=\frac34u,\qquad
u=\operatorname{tr}(A P_f).
```

These integrate to the unconditional branch probabilities $3/4$ and $1/4$; no branch is discarded. Measure the third specimen with the covariant POVM $3B\,dB$, whose likelihood is $\frac32(1-v)$, $v=\operatorname{tr}(B P_f)$.

For $c=\operatorname{tr}(AB)$, the unnormalized posterior ray matrices are

```math
\begin{aligned}
K_s(A,B)
&=\frac{(52+8c)I-(28+4c)A-20B+8(AB+BA)}{160},\\
K_a(A,B)
&=\frac3{160}[(4-c)I+4A-B-AB-BA].
\end{aligned}
```

Return a leading eigenvector of the relevant matrix. This is a global rule on the complete record, with bounded loss on every outcome. There is no localization event or omitted localization failure.

The symmetric matrix has largest eigenvalue

```math
\lambda_s(c)=\frac{13+2c}{40},
```

attained perpendicular to $\operatorname{span}(A,B)$. For the antisymmetric matrix, the nontrivial two-dimensional block of $4A-B-AB-BA$ has trace $3-2c$ and discriminant $25-24c$. Hence

```math
\lambda_a(c)
=\frac3{320}[11-4c+\sqrt{25-24c}].
```

Independent Haar rays have overlap density $2(1-c)$. The exact mean fidelity is

```math
\begin{aligned}
F_{\mathrm{cov}}
&=\int_0^1 2(1-c)[\lambda_s(c)+\lambda_a(c)]\,dc\\
&=\frac{41}{120}+\frac{463}{3600}
=\frac{1693}{3600}.
\end{aligned}
```

Covariance makes this fidelity constant over the wholly unknown true ray. Thus the continuous receiver has worst-case infidelity $1907/3600$.

### Fixed finite quantum measurements

The same posterior rule works with the twelve qutrit MUB rays $\psi_\ell$. Set $A_\ell=|\psi_\ell\rangle\langle\psi_\ell|$. For the pair use the 24 effects

```math
E_\ell^+=\frac12
|\psi_\ell\psi_\ell\rangle\langle\psi_\ell\psi_\ell|,
\qquad
E_\ell^-=\frac14
|g(\psi_\ell)\rangle\langle g(\psi_\ell)|,
```

where $g(f)=(\overline f_2,-\overline f_1,\overline f_0)$ in the normalized wedge basis
$(|0\rangle\wedge|1\rangle,|0\rangle\wedge|2\rangle,|1\rangle\wedge|2\rangle)$.
The antisymmetric outcome is labelled by $A_\ell$ in **dark-ray space**. This mapping matters: using $\psi_\ell$ literally in both physical bases need not give the same overlap table.

The 2-design identities imply $\sum_\ell E_\ell^\pm=P_\pm$. The final one-copy effects are $A_m/4$, twelve outcomes. The record $(\pm,\ell,m)$ has likelihood $h_\pm(u)\frac32(1-v)/144$, so the output rule above applies.

Under the uniform product weights of the two twelve-ray lists,

```math
c=1,\ 0,\ 1/3
\quad\text{have weights}\quad
1/12,\ 1/6,\ 3/4.
```

Its Haar mean fidelity is therefore

```math
\begin{aligned}
F_{\mathrm{MUB}}
&=\sum_{c\in\{1,0,1/3\}}w_c[\lambda_s(c)+\lambda_a(c)]\\
&=\frac{41}{120}+\frac{127+9\sqrt{17}}{1280}.
\end{aligned}
```

Choose one known independent Haar laboratory unitary $U$ before the experiment; conjugate both quantum measurements and the precomputed output rays by $U$, retaining $U$ in the classical record. This makes the finite-measurement protocol's risk constant over $f$. The quantum POVMs have 24 and 12 outcomes; the random laboratory setting remains continuous. An exact finite Haar setting list is not asserted. The [finite implementation](implementation.md) instead gives a constructive approximation using 2304 fair bits, finite rotations, a deterministic fallback and a uniform error bound that preserves the strict gap.

If the implemented rotation $V$ satisfies $\|U-V\|_{\mathrm{op}}\le\epsilon$, telescoping the three input conjugations and the output projector gives a conservative uniform risk change at most $8\epsilon$. Finite control precision can thus be included in the strict gap. The [receiver account](receiver.md) states implementation and calibration assumptions; the ideal theorem does not certify an arbitrary unknown apparatus.

## 3. A certificate covering every adaptive one-copy strategy

The comparator uses Haar averaging only to lower-bound worst-case risk. This supplies no orientation information to the experiment.

### From complete histories to a PPT seed

A complete history of a fresh-one-copy adaptive protocol induces a product of three positive local effects on the input specimens. Summing histories or randomizing outputs preserves full separability. Its output-ray effects are therefore positive under partial transpose (PPT) across every specimen cut.

Average the complete protocol over a known Haar laboratory rotation. Its Haar mean fidelity is unchanged and its output-ray POVM becomes covariant. At the base guessed ray $H=|0\rangle\langle0|$, write its seed as $\Omega$. It satisfies

```math
\Omega\succeq0,\qquad
\mathcal T_{U(3)}(\Omega)=I,\qquad
\Omega^{T_j}\succeq0\quad(j=1,2,3).
```

Average the seed over the stabilizer $K=U(1)\times U(2)$ of $H$, then over specimen permutations. These operations preserve the objective and normalization. Local-unitary conjugation preserves PPT. A permutation exchanges the three PPT cuts, so averaging preserves PPT when all cuts were imposed initially.

After permutation averaging, positivity of $\Omega^{T_1}$ implies positivity for the other singleton cuts by conjugation. A two-specimen transpose is a full transpose after the complementary singleton transpose; full transpose preserves positivity. Thus one displayed PPT constraint suffices for the twirled seed. The twirled measurement need not preserve a particular adaptive order: it is used only in a relaxation containing the comparator.

### The complete nine-block seed algebra

Put

```math
B=\int \rho_f^{\otimes3}|f_0|^2\,df,
\qquad C=S_{12}+S_{13}+S_{23}.
```

The Schur–Weyl sectors have $U(3)$ dimensions $1,8,10$, permutation multiplicities $1,2,1$, and central eigenvalues $C=-3,0,3$. Commutation with permutations forces the seed to be identity on the permutation multiplicity registers.

Within a sector, the number $n_0$ of dark-basis indices and the bright $SU(2)$ spin distinguish the $K$ types. Each occurs once on the $U(3)$ register. Explicitly, the collective bright-spin Casimir has eigenvalue $j(j+1)$ on each displayed block; its rank is exactly $(2j+1)$ times the permutation multiplicity. Together with $n_0$, these checks identify one irreducible stabilizer representation per block, so there is no unlisted seed degree of freedom. In particular, the mixed sector at $n_0=1$ splits into the bright symmetric spin-one and antisymmetric spin-zero representations. This is the small-dimensional multiplicity-free $U(3)$ to $U(1)\times U(2)$ branching. The resulting algebra has nine orthogonal blocks:

| $C$ | $B$ eigenvalue | $n_0$ | Bright spin | Full rank |
|---:|---:|---:|---:|---:|
| $-3$ | $0$ | 1 | $0$ | 1 |
| $0$ | $1/160$ | 2 | $1/2$ | 4 |
| $0$ | $1/120$ | 1 | $1$ | 6 |
| $0$ | $1/80$ | 1 | $0$ | 2 |
| $0$ | $1/60$ | 0 | $1/2$ | 4 |
| $3$ | $1/120$ | 3 | $0$ | 1 |
| $3$ | $1/80$ | 2 | $1/2$ | 2 |
| $3$ | $1/60$ | 1 | $1$ | 3 |
| $3$ | $1/48$ | 0 | $3/2$ | 4 |

The $B$ eigenvalues distinguish the blocks within each $C$ sector. Their projectors $R_i$ are Lagrange polynomials in $B,C$, with rational entries. Every allowed twirled seed is

```math
\Omega=\sum_i x_iR_i,\qquad x_i\ge0.
```

Haar-twirl normalization becomes

```math
\sum_{i:C_i=c}x_i\operatorname{rank}R_i=d_c,
\qquad(d_{-3},d_0,d_3)=(1,16,10).
```

For example, the mixed sector has an eight-dimensional $U(3)$ register and a two-dimensional permutation register, giving $d_0=16$. The fully antisymmetric sector has no target-state support, but its seed variable still affects PPT feasibility and cannot be dropped.

The comparator's Haar fidelity is at most the optimization over

```math
x_i\ge0,\quad
\sum_{i:C_i=c}x_i\operatorname{rank}R_i=d_c,\quad
\sum_i x_iR_i^{T_1}\succeq0,
```

with objective $\sum_i x_i\operatorname{tr}(BR_i)$. This relaxation includes PPT measurements beyond the adaptive one-copy class.

### A rational feasible dual

Take

```math
(\lambda_{-3},\lambda_0,\lambda_3)
=\left(
-\frac{1394413}{100000000},
\frac{838221}{50000000},
\frac{2083633}{100000000}
\right).
```

The exact rational $27\times27$ matrix $Y$ is supplied in
[the certificate](../verification/ppt_n3_certificate.json). It obeys

```math
Y\succeq0,\qquad
\lambda_{C_i}\operatorname{rank}R_i
-\operatorname{tr}(BR_i)
-\operatorname{tr}(Y R_i^{T_1})\ge0
\quad\text{for every }i.
```

The exact LDL decomposition of $Y$ has strictly positive pivots, the smallest $1/1000000$. The smallest of the nine scalar slacks is $599/300000000>0$.

For every feasible seed,

```math
\begin{aligned}
\operatorname{tr}(B\Omega)
&\le\sum_c\lambda_cd_c-\operatorname{tr}(Y\Omega^{T_1})\\
&\le\lambda_{-3}+16\lambda_0+10\lambda_3\\
&=\frac{46264989}{100000000}.
\end{aligned}
```

This proves the upper fidelity bound for the entire comparator. A numerical SDP discovered the certificate; its numerical optimum is not used in the proof.

## 4. Exact reproduction and limits

Run [the standalone verifier](../verification/check_finite_budget.py):

~~~bash
python verification/check_finite_budget.py
~~~

It uses only Python and SymPy. It reconstructs $B$ from exact Haar moments and all nine rational projectors, checks their spectra, ranks, orthogonality, dark-index counts, stabilizer commutation, bright-spin Casimirs and permutation invariance, and recomputes the saved dual's LDL decomposition and inequalities. It also derives both three-specimen posterior matrices by polynomial integration, integrates the covariant fidelity, checks the finite-MUB expression, and checks the two-specimen collective certificate and matching score. It does not load an SDP solution or call an optimizer.

The moment identity used throughout is

```math
\int\prod_{j=0}^{2}|f_j|^{2\alpha_j}\,df
=\frac{2\prod_j\alpha_j!}{(|\alpha|+2)!}.
```

Monomials with unequal ket and bra counts for any index integrate to zero. Expanding $(I-P_f)^{\otimes n}/2^n$ and multiplying by $|f_0|^2$ constructs every entry of $B$ rationally.

The guarantee depends on the equal-population, exact-rank-two source promise and a known laboratory reference. It concerns specimen risk, not laboratory time or hardware cost. Receiver imperfections and calibration failures must be added through their actual model and charged ledger.

