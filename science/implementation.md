# Finite randomization, control precision, and receiver resources

The three-specimen separation can be implemented with finitely many fair random bits, a fixed 24-outcome pair POVM, a fixed 12-outcome one-specimen POVM, and finite control precision. Its scientific content is the finite-risk separation proved in [the finite-budget account](finite-budget.md), not the existence of a POVM dilation. This page supplies the implementation and error budget needed to turn the ideal covariant comparison into a finite apparatus statement.

The control model permits arbitrary calibrated qutrit rotations and selective two-level unitaries on the stated finite qutrit–ancilla register. This is a finite joint-control construction, not a claim that a particular platform implements it economically. Actual control calibration must establish the stated error bounds; finite numerical descriptions do not certify a laboratory device.

## Fixed quantum outcomes

Let the twelve rays be the four standard qutrit mutually unbiased bases. Besides the three laboratory basis vectors, use

```math
\psi_{AB}=\frac1{\sqrt3}\sum_{j=0}^2\omega^{Aj^2+Bj}|j\rangle,
\qquad A,B\in\{0,1,2\},\quad \omega=e^{2\pi i/3}.
```

Their equal-weight projective 2-design identities give the following complete pair POVM:

```math
E_l^+=\frac12|\psi_l\psi_l\rangle\langle\psi_l\psi_l|,
\qquad
E_l^-=\frac14|g_l\rangle\langle g_l|,
```

where the normalized antisymmetric vector has wedge coordinates

```math
g_l=(\overline\psi_{l,2},-\overline\psi_{l,1},\overline\psi_{l,0})
\quad\text{in }(|0\rangle\wedge|1\rangle,
|0\rangle\wedge|2\rangle,|1\rangle\wedge|2\rangle).
```

Thus $\sum_lE_l^+=P_+$ and $\sum_lE_l^-=P_-$. The last specimen uses $F_l=|\psi_l\rangle\langle\psi_l|/4$, whose sum is $I_3$. Both pair branches, all last-specimen outcomes, and the setting are retained. There is no herald-and-repeat rule or discarded branch.

For a common setting $U$, rotate each input by $U^\dagger$, run these fixed POVMs, apply the posterior-eigenray decision rule to the two recorded MUB labels, and rotate that reported ray by $U$. The rotation of the reported ray is classical processing of its coordinates, not a fourth quantum specimen or a quantum output preparation.

The exact Haar-twirled fidelity is

```math
F_\mathrm{MUB}=\frac{41}{120}+\frac{127+9\sqrt{17}}{1280}.
```

The comparator certificate gives $R_\mathrm{one}\ge 53735011/10^8$. Consequently its strict risk margin over the ideal MUB receiver is

```math
\Delta=\frac{53735011}{10^8}-\bigl(1-F_\mathrm{MUB}\bigr)>0.0072.
```

The pair architecture and MUB identities are inherited ingredients. The onset theorem and its full-comparator certificate supply the operational distinction.

## A constructive finite replacement for a Haar setting

No unlisted exact finite unitary 4-design is assumed. The following finite algorithm approximates one common Haar setting with a uniform risk guarantee. All randomization is performed before the three specimen calls. It never requests another specimen when a classical draw is poorly conditioned.

Choose $T\ge1$, $0<a\le1$, and $0<\epsilon\le1/2$. Put

```math
\gamma=\frac{a^3}{18T^2},\qquad h=\frac{\gamma\epsilon}{8},\qquad
\phi(x)=\frac{e^{-x^2/2}}{\sqrt{2\pi}}.
```

Choose an integer $B$ satisfying $2^{-B}\le h\phi(T+1)/2$.

1. Draw eighteen independent $B$-bit integers $R_j$, each uniform on $\{0,\ldots,2^B-1\}$.
2. Compute each Gaussian quantile $\Phi^{-1}((R_j+1/2)2^{-B})$ to absolute error at most $h/4$. A certified inverse-CDF calculation followed by rounding to a sufficiently fine dyadic grid gives a finite rational description. Assemble these numbers as the real and imaginary entries of a $3\times3$ matrix $H$.
3. If $s_\min(H)<\gamma/2$, choose the identity setting. Otherwise form the polar unitary $V=H(H^\dagger H)^{-1/2}$ and produce a known finite-angle unitary program $W$ with $\|W-V\|_\mathrm{op}\le\epsilon/4$. Require its actual physical qutrit rotation $\widetilde W$ to satisfy the separately certified uniform control bound $\|\widetilde W-W\|_\mathrm{op}\le\epsilon/4$. Apply $\widetilde W^\dagger$ to the three specimens; use the known program $W$ in the classical ray conversion. The inverse-CDF, singular-value test, polar computation and angle compilation are classical operations before acquisition. The physical bound is a receiver assumption or a result of a separately charged control calibration, rather than an assertion that a finite numerical description has certified a device.

The scalar approximations in step 2 can instead use any certified error smaller than $h/4$. A discrete grid need not represent an exact Gaussian distribution. It is the coupling below, rather than an assertion of exact Haar sampling from finite bits, that controls the risk.

For completeness, the quantile subroutine has a terminating finite construction. Every requested probability lies between $2^{-B-1}$ and $1-2^{-B-1}$. Choose a rational $L$ larger than $\sqrt{2(B+2)\log2}+1$; Gaussian tail bounds place every requested quantile in $[-L,L]$. Bisect this interval using certified Gaussian-CDF intervals. At a midpoint whose CDF interval contains the requested probability, refine the CDF until its width divided by a certified lower bound for $\phi(L)$ is below $h/4$, then return that midpoint. Otherwise retain the appropriate half interval. The Gaussian integral is computable by convergent series with remainder bounds, so both branches terminate with a certified positional error. Rounding to a dyadic grid can be included within the same $h/4$ tolerance. The singular-value comparison for rational $H$ is likewise decidable by exact characteristic-polynomial root isolation of $H^\dagger H$, treating equality as a fallback. On the retained branch its gap from zero permits certified finite-precision square-root, polar and Givens-angle computations.

### Coupling proof

Couple the finite integers to independent continuous uniforms $X_j$ by $R_j=\lfloor 2^B X_j\rfloor$, and set $G_j=\Phi^{-1}(X_j)$. The exact complex Gaussian matrix $G$ has independent standard-normal real and imaginary entries. Its polar unitary $U$ is Haar: left unitary multiplication preserves the Gaussian law and commutes with the polar map.

Except on an event of probability at most $36e^{-T^2/2}$, all eighteen real Gaussian coordinates satisfy $|G_j|\le T$. On this event, the quantile arguments differ by at most $2^{-B-1}$. The chosen $B$ keeps the intermediate quantiles in $[-T-1,T+1]$, where the inverse-CDF derivative is at most $1/\phi(T+1)$. Including the numerical quantile error gives coordinate error at most $h/2$, hence

```math
\|H-G\|_\mathrm{op}\le\|H-G\|_F\le\frac{3h}{\sqrt2}.
```

The following elementary conditioning bound avoids requiring a singular-value distribution formula. Perform exact Gram–Schmidt on the three columns of $G$. Conditionally on earlier columns, each new orthogonal residual is an isotropic complex Gaussian vector in a subspace of dimension at least one. Its norm is at least the modulus of any one normalized complex coordinate, so the probability that its norm is below $a$ is at most $1-e^{-a^2/2}\le a^2/2$. A union bound gives three residual norms at least $a$ except with probability $3a^2/2$. On the coordinate-bound event,

```math
|\det G|\ge a^3,\qquad \|G\|_F^2\le18T^2,
\qquad s_\min(G)\ge\frac{a^3}{18T^2}=\gamma.
```

Indeed, $s_\min(G)=|\det G|/(s_1(G)s_2(G))$ and $s_1s_2\le\|G\|_F^2$. Therefore the fallback is not used on this good event.

For invertible matrices, the polar factors obey

```math
\|\operatorname{polar}(G)-\operatorname{polar}(H)\|_\mathrm{op}
\le\frac{2\|G-H\|_\mathrm{op}}{s_\min(G)+s_\min(H)}.
```

A short proof is useful here. Write $G=UA$, $H=VB$, $Q=U^\dagger V$ and $D=U^\dagger(G-H)=A-QB$. The matrix $C=I-Q$ solves $AC+CB=D-D^\dagger Q$. Integrating the Sylvester equation gives $C=\int_0^\infty e^{-tA}(D-D^\dagger Q)e^{-tB}\,dt$ and the displayed bound. Weyl's inequality and the choice of $h$ now give $s_\min(H)\ge\gamma/2$ and $\|V-U\|_\mathrm{op}<\epsilon/2$. Including both finite-angle compilation and physical rotation errors gives $\|\widetilde W-U\|_\mathrm{op}\le\epsilon$, while the classically used program obeys $\|W-U\|_\mathrm{op}<3\epsilon/4$.

The resulting coupling has failure probability

```math
\delta_\mathrm{rand}\le36e^{-T^2/2}+\frac32a^2.
```

At failure the protocol still uses exactly three specimens, keeps every record and returns a ray; its loss is bounded by one. A conditioning failure is therefore charged in risk, not hidden in an unlimited retry procedure.

### From setting error to score error

Replacing the ideal input rotation $U$ by the physical $\widetilde W$ changes each rotated input state in trace norm by at most $2\epsilon$. Telescoping three tensor factors gives at most $6\epsilon$. The reported ray uses the known program $W$, whose output projector differs from the ideal $U$ output in operator norm by at most $2\epsilon$. Consequently a conservative uniform bound for the complete expected infidelity is

```math
R_\mathrm{finite}\le1-F_\mathrm{MUB}+8\epsilon+\delta_\mathrm{rand}.
```

This bound is uniform in the unknown dark ray and includes the failed-setting event. It is a finite-sample statement at three total source specimens, not an asymptotic design argument.

For example, take $T=8$, $a=1/100$, $\epsilon=10^{-4}$ and $B=128$. Then $\gamma=1/(1\,152\,000\,000)$, $h=\gamma/80000$, the inverse-CDF condition holds, and only $18B=2304$ fair random bits are needed. The added risk is below $0.000951$, well within $\Delta>0.0072$.

## Explicit finite Naimark construction

For either fixed POVM, write its rank-one effects as $E_y=|v_y\rangle\langle v_y|$. Form the matrix $J$ whose row $y$ is $v_y^\dagger$. Completeness gives $J^\dagger J=I$. This is an explicit isometry, with all fixed entries algebraic numbers from the qutrit MUB.

For the pair, pad the $24\times9$ isometry with twelve zero rows to a $36\times9$ isometry. The physical register consists of the two qutrits and two initialized qubits, of total dimension $9\times4=36$. Complete the isometry columns to a $36\times36$ unitary by orthogonalizing the standard basis and skipping zero residuals. Measuring the full register in its product basis realizes the twenty-four labels; twelve labels have zero ideal probability. Unexpected labels from an imperfect apparatus remain recorded and have a specified fallback ray.

For the final specimen, the $12\times3$ isometry is extended to a $12\times12$ unitary on one qutrit and two initialized qubits. The same two physical ancilla qubits may be reset and reused after the pair measurement. They carry no coherent information into the third-specimen experiment.

A $D$-dimensional unitary is constructively reduced to at most $D(D-1)/2$ selective two-level Givens blocks and $D$ diagonal phases. This already gives finite upper bounds of 630 mixing blocks and 36 phases for the pair dilation, and 66 blocks and 12 phases for the single dilation. A more economical direct construction eliminates only the $d$ supplied isometry columns. It needs at most $dD-d(d+1)/2$ mixing blocks and $d$ phases: 279 blocks and 9 phases for $d=9,D=36$, and 30 blocks and 3 phases for $d=3,D=12$. The inverse elimination sequence explicitly defines a full unitary with the required first columns. These are joint controls on the stated register, not a claim that each is a one-qutrit gate. A three-angle description of every mixing block gives angle upper bounds of 846 and 93 for this direct construction. The three common qutrit rotations add at most 36 angle settings.

If each angle is implemented within $d$, telescoping the unitary factors bounds the dilation-unitary error by the number of angles times $d$. A compiled dilation error $\eta$ changes its classical measurement distribution in total variation by at most $\eta$ for every input state, by purification and trace-distance contractivity. Consequently errors $\eta_\mathrm{pair}$ and $\eta_\mathrm{single}$ add at most their sum to the risk. A final reported-projector error bounded by $\eta_\mathrm{out}$ adds at most $\eta_\mathrm{out}$.

The complete implementation guarantee is therefore

```math
R_\mathrm{actual}\le1-F_\mathrm{MUB}
+8\epsilon+\delta_\mathrm{rand}
+\eta_\mathrm{pair}+\eta_\mathrm{single}+\eta_\mathrm{out}.
```

The numerical example remains separated if each of the last three tolerances is $10^{-4}$. The total added risk is below $0.001251<\Delta$. For a device with additional certified operational error $\eta_\mathrm{other}$, add that quantity explicitly; it cannot be dismissed as numerical precision.

### The separate 450-outcome receiver

The large-budget memory/noise theorem uses the fixed weighted projective 4-design receiver, with 450 rank-one pair effects. The same row-isometry construction embeds its nine-dimensional input in dimension 450 using a 50-level ancilla. With qubit ancillas, six qubits give dimension $9\cdot64=576$; pad the 450 rows by 126 zero rows and read every product-basis label. Direct isometry elimination requires at most $9\cdot576-45=5139$ selective mixing blocks and 9 phases, or 15426 angle settings in the same description. This is a constant finite control count for a two-qutrit block, with substantially larger apparatus than the 24-outcome receiver. A uniform compiled-dilation operator error at most $\eta$ gives a uniform per-pair outcome total-variation bound at most $\eta$, including unexpected padded labels. Thus the separately declared total-variation tolerance in [the memory/noise theorem](memory-noise.md) can be obtained from a certified dilation-control bound. It is not inferred from the memory-strength binomial test.

## Resource ledger and calibration boundary

|Resource|Three-specimen implementation|
|---|---|
|Unknown-source calls|Exactly three, including every measured branch|
|Stored unknown system|One qutrit held for one preparation interval, then through pair control/readout|
|Other unknown specimens|Second qutrit joins the stored qutrit; third is measured separately|
|Coherent joint control|One 36-dimensional pair-register unitary; no quantum memory joins the third specimen to the pair|
|Ancillas|Two initialized qubits for the pair; reset and reuse for the final single readout|
|Readout|One complete pair-register readout and one complete single-register readout; all nominal and unexpected labels retained|
|Classical setting|One common finite setting, generated before acquisition; 2304 fair bits in the explicit example|
|Classical processing|Finite inverse-CDF/polar compilation and one posterior-eigenray lookup; numerical output precision is charged|
|Failed classical draw|Identity fallback; three source calls still made and its probability contributes to the risk|
|Calibration/reference calls|Zero only under the stated known-reference and certified-control assumptions; any experiment learning those bounds uses the separately specified calibration budget|

Neither a floating-point check nor a finite-angle description proves the physical tolerances. If receiver errors or the laboratory frame are unknown, a calibration theorem must provide the required bound and count its reference specimens, confidence failures, storage and operations in the total budget. The three-specimen theorem is a known-reference result; it must not be re-labelled a three-call theorem after uncounted external calibration. See the separate noise/calibration account for the model actually being learned.

Specimen advantage is the claimed resource distinction. Control duration, laboratory time, ancilla hardware, receiver complexity and calibration cost are separate quantities, and no superiority in those quantities follows from the specimen theorem.
