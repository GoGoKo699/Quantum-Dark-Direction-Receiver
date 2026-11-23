# The exact three-qutrit measurement hierarchy

Three specimens from $`\rho_f=(I-P_f)/2`$ already distinguish four levels of measurement access. The loss is $`1-\mathrm{tr}(\widehat P P_f)`$ for the reported ray projector $`\widehat P`$. Every specimen is used and every outcome contributes to the risk. The reference is known and the measurement controls in this comparison are ideal. See the [source model](model.md).

| Measurement access at three specimens | Optimal worst-case infidelity |
|---|---:|
| Unrestricted collective | $`21/40=0.525000`$ |
| POVM with biseparable effects | $`39/64-\sqrt{6001}/960\approx0.528681`$ |
| Fixed-cut separable, including randomization over complete fixed-cut POVMs | $`109/192-3\sqrt{17}/320\approx0.529054`$ |
| Sequential pair then single, or single then pair | $`109/192-3\sqrt{17}/320\approx0.529054`$ |
| Adaptive single-copy | At least $`0.53735011`$ |

A positive effect is **separable across a fixed cut** if it is a sum of positive products across that cut. A **biseparable effect** is a sum of such products, with the cut allowed to vary among its terms. For a fixed-cut POVM, one cut applies to the full normalized measurement. A random choice among complete fixed-cut POVMs has the same optimal fidelity as a fixed-cut POVM here, since all cuts are equivalent under permutation of the specimens. The larger class with biseparable effects imposes the cone constraint on each outcome effect and normalizes the effects jointly. This difference in normalization leads to the strict gap in the table.

Yi et al. call a coarse graining of a random choice among complete fixed-cut separable POVMs a biseparable POVM. Their pure-qubit problem has different optima for the two sequential orders. Here both orders attain the fixed-cut optimum, and the larger class with biseparable effects improves on both. [Yi et al., Secs. II–III](https://arxiv.org/html/2412.03383v2).

## Score and the unrestricted optimum

Use Haar ray measure $`df`$ of mass one. For guessed ray projector $`G`$, the score operator is

```math
B_G=\int \rho_f^{\otimes3}\,\mathrm{tr}(G P_f)\,df.
```

For effects $`E_y`$ and guesses $`G_y`$, the Haar mean fidelity is $`\sum_y\mathrm{tr}(B_{G_y}E_y)`$. Sums can also be integrals against a POVM density. The worst-case fidelity is at most the mean. Jointly rotating the protocol and its guesses by one known Haar laboratory unitary makes the mean uniform over $`f`$. Common rotations preserve each comparison class, including either sequential order.

Let $`P_{\mathrm{sym}}`$, $`P_{\mathrm{mix}}`$ and $`Q`$ project onto the fully symmetric, mixed and fully antisymmetric sectors of three qutrits. Their ranks are $`10,16,1`$. The [nine score blocks](finite-budget.md#the-complete-nine-block-seed-algebra) give

```math
Y=\frac{P_{\mathrm{sym}}}{48}+\frac{P_{\mathrm{mix}}}{60},
\qquad
D_G=Y-B_G\succeq0,
\qquad
\mathrm{tr}(Y)=\frac{19}{40}.
```

The equality subspace of the score bound consists of $`(G^\perp)^{\otimes3}`$ and the determinant line $`Q`$, where $`G^\perp`$ denotes the plane perpendicular to the range of $`G`$. In the symmetric and mixed sectors, the intersection with $`(G^\perp)^{\otimes3}`$ has rank four in each case. Weighting the two intersection projectors by $`10/4`$ and $`16/4`$, and adding $`Q`$, gives a seed that rotates into a normalized covariant POVM. Its effect is proportional to the identity on each permutation multiplicity space before rotation. Schur averaging therefore normalizes each sector by its trace. It attains mean fidelity $`19/40`$ and has constant risk. The [all-budget theorem](collective-minimax.md) gives the same value.

The determinant line has zero input probability for every $`f`$. It still contributes to measurement completeness. In particular, for every complete POVM the total weight $`\sum_y\mathrm{tr}(QE_y)`$ is one. A product effect across a cut can cover that line only while putting some additional weight outside the equality subspace. The restricted optima turn on the least possible cost of covering the line.

## Exact bounds for separable effects

Fix the cut $`1|23`$ and let $`C_-`$ project onto the antisymmetric sector of the pair $`23`$ with identity on specimen $`1`$. The score, the three sector projectors and $`Q`$ commute with the pair SWAP. In evaluating their traces, a rank-one product effect can therefore be split into symmetric and antisymmetric pair pieces. The symmetric piece has nonnegative deficit and zero determinant weight. The antisymmetric piece lies in $`P_{\mathrm{mix}}+Q`$.

For a normalized single-specimen vector and an antisymmetric pair vector, use a basis preserving the guessed ray $`G=|0\rangle\langle0|`$ to write

```math
|a\rangle=\sqrt t\,|0\rangle+\sqrt{1-t}\,|1\rangle,
\qquad
|\psi\rangle=x|w_{12}\rangle+y|w_{02}\rangle+z|w_{01}\rangle,
\qquad
|w_{ij}\rangle=(|ij\rangle-|ji\rangle)/\sqrt2 .
```

The determinant weight of $`|a\rangle|\psi\rangle`$ is

```math
b=\frac{|\sqrt t\,x-\sqrt{1-t}\,y|^2}{3},
```

because the normalized determinant vector is proportional to $`|0\rangle|w_{12}\rangle-|1\rangle|w_{02}\rangle+|2\rangle|w_{01}\rangle`$, with normalization $`1/\sqrt3`$. In the one-dark-index subspace, $`|0\rangle|w_{12}\rangle`$ is a bright-spin singlet, $`|1\rangle|w_{02}\rangle`$ has equal singlet and triplet weights, and $`|1\rangle|w_{01}\rangle`$ is a triplet orthogonal to the latter triplet component. Removing the determinant weight leaves the mixed singlet weight. The mixed singlet, mixed triplet and two-dark-index mixed subspaces have deficits per unit weight $`1/240`$, $`1/120`$ and $`1/96`$, respectively. The zero-dark-index subspace has zero deficit. Substitution gives

```math
240\langle a,\psi|D_G|a,\psi\rangle
=t|x|^2+(3/2+t)|y|^2+(2+t/2)|z|^2-b.
```

For $`\eta>0`$, define

```math
p_\eta(t)=\frac{t}{t+\eta}+\frac{1-t}{3/2+t+\eta},
\qquad
c_\eta=\frac{3}{\max_{0\le t\le1}p_\eta(t)} .
```

Cauchy–Schwarz with weights $`t+\eta`$ and $`3/2+t+\eta`$ bounds $`3b`$ by $`p_\eta(t)[(t+\eta)|x|^2+(3/2+t+\eta)|y|^2]`$. Together with the nonnegative $`z`$ contribution this yields

```math
240\langle a,\psi|D_G|a,\psi\rangle
\ge (c_\eta-1)b-\eta\langle\psi|\psi\rangle .
```

The same inequality holds for any cut by relabeling the specimens. For an effect separable across the fixed cut $`1|23`$, extending by linearity gives

```math
240\,\mathrm{tr}(D_G E)
\ge (c_\eta-1)\,\mathrm{tr}(QE)-\eta\,\mathrm{tr}(C_- E).
```

Here $`\mathrm{tr}(C_-E)`$ is the total antisymmetric pair weight after splitting the product terms. For a biseparable effect with varying cuts, the total antisymmetric pair weight is bounded by $`\mathrm{tr}[(P_{\mathrm{mix}}+Q)E]`$. Indeed, each antisymmetric pair term lies entirely in those two sectors and dropping the symmetric terms only decreases their combined trace. This yields the cut-independent inequality with $`P_{\mathrm{mix}}+Q`$ in place of $`C_-`$. The effect inequalities also apply to continuous outcomes by linearity and closure of the separable cones.

Completeness now gives mean fidelity at most

```math
\frac{19}{40}-\frac{c_\eta-1-M\eta}{240},
\qquad
M=\begin{cases}
9 & \text{fixed cut},\\
17 & \text{biseparable effects}.
\end{cases}
```

Here $`9=\mathrm{tr}(C_-)`$ and $`17=\mathrm{tr}(P_{\mathrm{mix}}+Q)`$. The fixed-cut bound also holds for random mixtures of complete fixed-cut POVMs and any coarse graining of their outcomes.

### Choosing the scalar certificate

For either $`M`$, take the larger root $`u`$ of $`18(u+1)^2=25Mu`$ and set $`\eta=(5/2)/(u^2-1)`$. In the two cases

```math
u_9=\frac{21+5\sqrt{17}}{4},
\qquad
u_{17}=\frac{389+5\sqrt{6001}}{36}.
```

The derivative is $`p_\eta'(t)=\eta/(t+\eta)^2-(5/2+\eta)/(3/2+t+\eta)^2`$. Its sign is positive before and negative after the unique interior maximum at $`t_*=(3u/2-1)/(u^2-1)`$. This follows because $`(3/2+t+\eta)/(t+\eta)`$ decreases through $`u`$. Evaluating at $`t_*`$ gives $`c_\eta=9(u+1)/[5(u-1)]`$. Substitution in the complete-measurement bound gives

```math
F_{\mathrm{fixed}}\le \frac{83}{192}+\frac{3\sqrt{17}}{320},
\qquad
F_{\mathrm{effects}}\le \frac{25}{64}+\frac{\sqrt{6001}}{960}.
```

### Attaining the optimum with biseparable effects

Use $`u_{17},t_*,\eta`$ in the product above and take normalized coefficients proportional to

```math
(x,y,z)=\left(
 \frac{\sqrt{t_*}}{t_*+\eta},
 -\frac{\sqrt{1-t_*}}{3/2+t_*+\eta},
 0
\right).
```

They saturate the weighted Cauchy–Schwarz bound. The determinant weight after normalization is $`b=25u/[18(u+1)^2]=1/17`$. Since the pair is antisymmetric, the remaining weight $`16/17`$ is mixed. For guess $`|0\rangle`$, use the seed

```math
\Omega=17|a,\psi\rangle\langle a,\psi|+10|111\rangle\langle111|.
```

The second term supplies the full symmetric trace and has zero deficit. The three sector traces are $`10,16,1`$, so twirling the seed by common $`U(3)`$ rotations and permutations gives identity. The measurement has each rotated and permuted seed as its effect density with respect to the normalized product measure. It reports the rotated ray $`U|0\rangle`$. Its individual effects are biseparable, and every seed saturates the upper bound for that class. Common rotational covariance gives constant risk. Normalization uses the total sector traces across the permuted seeds, while the fixed-cut constraint would require a complete POVM within a single cut.

## Both sequential orders attain the fixed-cut optimum

A sequential protocol measures one block and then the other while communicating its classical record. For either order the full-history effects are products across the same cut. The fixed-cut upper bound therefore applies in either direction, including adaptive choices of the second POVM. The following receivers attain it.

Split the pair POVM by SWAP parity and refine its effects to rank one within each block. This is permitted because the pair signals commute with SWAP. Use rank-one single-specimen effects as well. In the symmetric branch choose pair rays of the form $`|A,A\rangle`$ in a POVM on the symmetric pair sector, for example the continuous coherent POVM $`6|A,A\rangle\langle A,A|\,dA`$. Choose any complete single-specimen rank-one POVM in this branch. Given a pair ray $`A`$ and a single ray $`B`$, report a ray orthogonal to both. The product effect then lives entirely in the score equality subspace. The total effects in this branch sum to identity on the single specimen times the symmetric pair projector. The score is

```math
\frac{10}{48}+\frac{8}{60}=\frac{41}{120}.
```

The rank eight arises because the transposition on the pair has one symmetric and one antisymmetric direction in the two-dimensional mixed-sector permutation representation. The symmetric pair branch includes its symmetric direction.

In the antisymmetric branch, let $`A`$ label the pair ray via the conjugate Hodge identification and $`B`$ label the single ray. Write $`c=\mathrm{tr}(P_A P_B)`$. For effect weights $`w_A,w_B`$, the [posterior calculation](finite-budget.md#2-a-three-specimen-attaining-strategy) gives the optimal score contribution $`w_Aw_B\lambda_a(c)/9`$, with

```math
\lambda_a(c)=\frac{3}{320}\left(11-4c+\sqrt{25-24c}\right).
```

The factor $`1/9`$ converts the Haar outcome convention, which uses total weights three for the antisymmetric pair and three for the single specimen, to the given effects. In either sequential order, completeness of the second measurement in this branch forces its weighted mean overlap with the first ray to be $`1/3`$. The strict concavity of $`\lambda_a`$ gives a score bound $`\lambda_a(1/3)`$. To attain it, measure the second ray in an orthonormal basis with overlap squared $`1/3`$ with the first ray. One can construct such a basis by choosing a frame with the first ray as an axis and taking its discrete Fourier basis. For a second measurement on the pair, use the conjugate Hodge images of those basis vectors in the antisymmetric sector. Report the leading posterior eigenray on every antisymmetric outcome.

For pair then single, choose the pair's antisymmetric basis first and choose the single basis using that record. For single then pair, choose the single basis first and choose the pair's antisymmetric basis using that record. In both cases the symmetric branch proceeds as above. The resulting total Haar fidelity is

```math
\frac{41}{120}+\lambda_a(1/3)
=\frac{41}{120}+\frac{29+3\sqrt{17}}{320}
=\frac{83}{192}+\frac{3\sqrt{17}}{320}.
```

Applying the common laboratory rotation yields this fidelity for every input ray and keeps each measurement order. This proves the exact sequential infidelities and attains the fixed-cut bound.

## Adaptive single-copy readout and implementation scope

The [released rational certificate](finite-budget.md#3-a-certificate-covering-every-adaptive-one-copy-strategy) bounds the fidelity of every adaptive single-copy receiver by $`0.46264989`$. It includes arbitrary one-copy measurements, biased estimates and adaptive use of classical histories. The fixed-cut fidelity exceeds that bound even with $`\sqrt{17}`$ replaced by $`4`$. The two restricted fidelity deficits below $`19/40`$ are $`(4+9/u_M)/1200`$. They are strictly positive, and $`u_{17}>u_9`$ gives the strict ordering between the two restricted optima. The precise single-copy optimum at three specimens remains open here.

This hierarchy uses the exact rank-two equal-population model with ideal known controls. [Finite-control implementation](implementation.md) concerns the earlier explicit pair receiver. [Paid calibration](calibration.md) treats a separate operating point with detector readout and memory assumptions.

