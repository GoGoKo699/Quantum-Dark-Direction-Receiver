# Paid calibration of the first-specimen memory

The receiver can retain a finite specimen advantage while paying for an independent memory check. The statement below concerns one specified, stationary depolarizing channel. The binomial test is standard; the result is its composition with the global receiver risk bound and the all-adaptive-one-copy lower bound at one total specimen budget.

## Experiment and assumptions

The unknown source emits independent qutrits

```math
\rho_f=\frac{I-P_f}{2},\qquad P_f=|f\rangle\!\langle f|,
\qquad f\in\mathbb{CP}^2.
```

The target is the ray $`f`$, with loss $`1-\mathrm{tr}(P_{\widehat f}P_f)`$. Its laboratory reference is known. In every signal or calibration pair, the first qutrit undergoes

```math
\mathcal D_\nu(T)=\nu T+(1-\nu)\mathrm{tr}(T)\frac I3,
\qquad 0\le\nu\le1,
```

while the second is fresh. The same unknown $`\nu`$ applies to all uses. Specimen preparations, channel environments and measurement outcomes are independent between pairs conditional on $`\nu`$. Thus stationarity alone, without this independence, is insufficient for the binomial and concentration bounds used here. Known reference preparation, the second qutrit and the specified pair measurement are ideal. Unknown coherent rotations, correlated memory noise and additional gate/readout errors are outside this model.

Use $`M`$ known pure calibration pairs $`P_0\otimes P_0`$, where $`P_0=|0\rangle\langle0|`$. Each calibration pair passes through the same first-qutrit memory and the same receiver used for the signals. Sum its antisymmetric outcomes to obtain $`A`$. Since the antisymmetric projector is $`P_-=(I-S)/2`$,

```math
\begin{aligned}
\Pr_\nu(-\mid P_0\otimes P_0)
&=\frac{1-\mathrm{tr}[\mathcal D_\nu(P_0)P_0]}2\\
&=\frac{1-\nu}{3}=:p_\nu,
\qquad A\sim\mathrm{Bin}(M,p_\nu).
\end{aligned}
```

These are known pure reference specimens, not free unknown-source samples. Both specimens in every reference pair count in the total budget. This experiment tests a parameter *within* the depolarizing model; it does not validate that model, reference preparation or stationarity.

## Exact finite calibration test

Take $`M=100000`$ and accept when $`A\le500`$, equivalently $`A/M\le q=1/200`$. Distinguish three hardware ranges:

| True memory parameter | Calibration guarantee |
|---|---|
| $`\nu\ge99/100`$ | False rejection probability at most $`\alpha_M`$ |
| $`49/50\lt \nu\lt 99/100`$ | No binary certification guarantee |
| $`\nu\le49/50`$ | False acceptance probability at most $`\beta_M`$ |

Writing $`D_{\mathrm{Ber}}`$ for Bernoulli relative entropy, the standard binomial Chernoff bound gives

```math
\begin{aligned}
\alpha_M
&=e^{-M D_{\mathrm{Ber}}(1/200\Vert1/300)}
=\left(\frac23\right)^{500}
 \left(\frac{598}{597}\right)^{99500}
\lt 10^{-15},\\
\beta_M
&=e^{-M D_{\mathrm{Ber}}(1/200\Vert1/150)}
=\left(\frac43\right)^{500}
 \left(\frac{596}{597}\right)^{99500}
\lt \frac{11}{10^{11}}.
\end{aligned}
```

Numerically these bounds are approximately $`1.8890\times10^{-16}`$ and $`1.0624\times10^{-10}`$. They are finite binomial bounds, not Gaussian confidence intervals. To obtain them, apply exponential Markov to $`\mathbb E e^{sA}=(1-p+pe^s)^M`$ and optimize over $`s>0`$ for the upper tail or $`s\lt 0`$ for the lower tail. Monotonicity of binomial tails in $`p`$ gives the uniform endpoints in the table. Using $`A\ge500`$ to bound the actual rejection event $`A\ge501`$ is conservative.

## Signal estimator and unconditional risk

Measure all $`K`$ unknown signal pairs with the fixed finite design receiver. For completeness, its symmetric and antisymmetric effects are

```math
E_\ell^+=6w_\ell|\psi_\ell\psi_\ell\rangle
 \!\langle\psi_\ell\psi_\ell|,
\qquad
E_\ell^-=3w_\ell P_{g(\psi_\ell)},
```

where $`(w_\ell,\psi_\ell)`$ is the specified normalized weighted projective 4-design and $`g`$ is the conjugate Hodge identification with the antisymmetric qutrit. Both parity branches and every outcome are retained. From outcome $`\ell`$ form

```math
Z=\begin{cases}
2I-5P_{\psi_\ell},&+,\\
4P_{\psi_\ell}-I,&-,\\
0,&\text{unexpected padding label}.
\end{cases}
```

Its mean is $`\mathbb EZ=((1+\nu)/2)P_f+((1-\nu)/6)I`$. Hence the principal eigenray of $`K^{-1}\sum Z`$ estimates $`f`$ without substituting an estimated $`\nu`$. This is why a calibration error does not enter a plug-in bias term.

If calibration accepts, return this principal eigenray. If it rejects, return a uniformly random one of the three computational rays, independently of all other records. This finite classical fallback has expected loss exactly $`2/3`$ for every $`f`$. Resolve any eigenvalue tie by a fixed convention. All $`K`$ signal pairs are still prepared and measured, including when calibration rejects, so the protocol has a deterministic charged budget.

The receiver's global moment and matrix-concentration argument gives, for $`0\lt t\lt (1+\nu_0)/4`$ and $`\nu\ge\nu_0`$,

```math
U(K,\nu_0,t)=
\frac{103-4\nu_0}
 {30K[(1+\nu_0)/2-2t]^2}
+6\exp\!\left[-\frac{Kt^2}{21/2+(8/3)t}\right].
```

This bound includes every large spectral-estimation error by assigning loss at most one on the concentration failure event. It requires no pilot localization. Calibration and signal records are independent conditional on $`\nu`$. For the actual performance range $`\nu\ge99/100`$, using the conservative signal parameter $`\nu_0=49/50`$ therefore yields the **unconditional** guarantee

```math
\sup_{f,\,\nu\ge99/100}\mathbb E_{f,\nu}\ell
\le U(K,49/50,t)+\frac23\alpha_M.
```

Indeed, with $`r_\nu=\Pr_\nu(\mathrm{reject})`$, risk is at most $`(1-r_\nu)U+(2/3)r_\nu\le U+(2/3)\alpha_M`$. This neither discards rejected calibrations nor conditions the performance claim on acceptance. The separate false-acceptance bound $`\beta_M`$ is certificate soundness for the bad-device range; it is not an additional risk term in the good-device theorem.

## A fully charged finite comparison

Choose

```math
M=100000,\quad K=1400000,\quad
B=2M+2K=3000000,\quad t=\frac1{80}.
```

The moment term and Bernstein exponent simplify exactly to

```math
\frac{103-4(49/50)}
 {30K[(1+49/50)/2-2/80]^2}
=\frac{2477}{977786250},
\qquad
\frac{Kt^2}{21/2+(8/3)t}=\frac{13125}{632}.
```

The risk bound is approximately $`2.539014429\times10^{-6}`$. For a certificate using rational arithmetic only, $`(1+x/n)^n\le e^x`$ gives

```math
\begin{aligned}
R_{\mathrm{paid}}
&\le\frac{2477}{977786250}
 +6\left(\frac{5056}{5161}\right)^{1000}
 +\frac{2}{3\cdot10^{15}}\\
&\lt \frac8{3000016}
\le\frac{16}{B+24+\sqrt{B(B+16)}}.
\end{aligned}
```

The rightmost expression lower-bounds the worst-case risk of **every** adaptive one-copy protocol with $`B`$ ideal unknown-source specimens. Thus the comparison grants that class all calibration expenditure as extra ideal signal specimens and still proves strict finite superiority. The exact rational inequalities and calibration bounds are checked by [the calibration certificate](../verification/check_calibration.py). The certificate checks the stated finite theorem; it does not estimate an optimal experimental crossover.

## Additional bounded receiver errors

An operational error bound can be included without adding the probability of any error over all $`K`$ readouts. Suppose that, for every permitted signal ray and every calibration reference, the actual complete pair-outcome distribution is within total variation $`\tau`$ of the stated ideal receiver after $`\mathcal D_\nu`$. The nominal outcome labels still determine the same matrix samples $`Z`$. Retain every unexpected Naimark-padding label, assign it $`Z=0`$ for signal accumulation and the fixed $`+`$ label for calibration counting, and extend the ideal distribution by zero on these labels before taking total variation. Thus no unexpected outcome is discarded. Pair records are independent and have the same actual distribution at fixed input and $`\nu`$. This is an externally established uniform implementation assumption. The parity check does **not** learn $`\tau`$, validate the depolarizing model or certify arbitrary control errors.

The [bounded-error analysis](memory-noise.md) gives the conservative signal bound below, weakening its $`25\tau/4`$ tangent perturbation to $`9\tau`$ for simpler constants:

```math
U_\tau(K,\nu_0,t)=
\frac{(V(\nu_0)+9\tau)/K+36\tau^2}
 {[b(\nu_0)-2t-12\tau]^2}
+6\exp\!\left[-\frac{Kt^2}{18+4t}\right],
\quad
V(\nu)=\frac{103-4\nu}{30},\quad b(\nu)=\frac{1+\nu}{2},
```

provided the denominator before squaring is positive. The $`36\tau^2`$ term retains receiver bias. More explicitly, the actual mean differs from the ideal mean by a matrix $`\Delta`$ with norm at most $`6\tau`$. Centering the sample mean at its actual expectation makes its cross term with this fixed bias vanish exactly; the numerator bounds variance divided by $`K`$ plus squared bias. The concentration failure is still assigned loss at most one. Thus a fixed receiver error leads to a bias floor; a bound of order $`\tau=O(B^{-1/2})`$ is appropriate for retaining a specified $`1/B`$ risk margin. A full-record union bound of order $`B\tau`$ is unnecessary for this moment estimator.

The actual calibration antisymmetric probability differs from $`(1-\nu)/3`$ by at most $`\tau`$. Use

```math
\begin{aligned}
\alpha_{M,\tau}
 &=e^{-M D_{\mathrm{Ber}}(1/200\Vert1/300+\tau)},\\
\beta_{M,\tau}
 &=e^{-M D_{\mathrm{Ber}}(1/200\Vert1/150-\tau)}.
\end{aligned}
```

These apply while the perturbed good endpoint is below $`1/200`$ and the perturbed bad endpoint is above it. They preserve the same good, indifference and bad ranges in $`\nu`$. The unconditional good-device risk becomes $`U_\tau+(2/3)\alpha_{M,\tau}`$; $`\beta_{M,\tau}`$ remains a separate bad-device soundness bound.

For the same $`M=100000`$, $`K=1400000`$ and $`B=3000000`$, take

```math
\tau=\frac1{100000},\qquad t=\frac9{500}.
```

The calibration endpoints are $`1003/300000`$ and $`1997/300000`$, and their exact Chernoff expressions are

```math
\begin{aligned}
\alpha_{M,\tau}
 &=\left(\frac{1003}{1500}\right)^{500}
   \left(\frac{298997}{298500}\right)^{99500}\lt 10^{-15},\\
\beta_{M,\tau}
 &=\left(\frac{1997}{1500}\right)^{500}
   \left(\frac{298003}{298500}\right)^{99500}
   \lt \frac{14}{10^{11}}.
\end{aligned}
```

The signal moment-and-bias term is exactly $`992339/382152562848`$ and its Bernstein exponent is exactly $`6300/251`$. A fully rational certificate is

```math
\begin{aligned}
R_{\mathrm{paid},\tau}
&\le\frac{992339}{382152562848}
 +6\left(\frac{2510}{2573}\right)^{1000}
 +\frac2{3\cdot10^{15}}\\
&\lt \frac8{3000016}\le L_B.
\end{aligned}
```

Its certified upper bound is approximately $`2.596811825\times10^{-6}`$, below the one-copy lower bound $`2.666652445\times10^{-6}`$. This accounts for a declared total-variation implementation error as well as the unknown first-specimen memory strength and the paid calibration failures. It does not claim that a particular device has achieved the declared error bound.

## Resource ledger and limits

| Resource | Charged amount |
|---|---:|
| Known pure reference specimens | $`2M=200000`$ |
| Unknown-source signal specimens | $`2K=2800000`$ |
| Total specimen preparations | $`B=3000000`$ |
| First-qutrit memory uses | $`M+K=1500000`$ |
| Complete pair readouts | $`M+K=1500000`$ |
| Coherent storage across preparation intervals | One qutrit per pair |
| Persistent quantum memory between pairs | None |
| Classical processing | Bounded-size matrix accumulation, one qutrit eigensystem, calibration count |

The finite design and its dilation require fixed finite coherent control and an outcome register. Operation counts and specimen advantage do not establish an advantage in laboratory duration, energy, implementation accuracy or hardware cost. The references require known laboratory preparation, and calibration specimens do not certify all properties of that preparation or receiver.

Superiority is uniform over the stated good-device range, not over arbitrary $`\nu`$. For $`\nu\le49/50`$, write $`\beta=\beta_M`$ for the ideal readout and $`\beta=\beta_{M,\tau}`$ for the declared-error readout. The corresponding protocol rejects with probability at least $`1-\beta`$, so its unconditional risk is at least $`(2/3)(1-\beta)`$ from the fallback alone. An acceptance certificate cannot turn the good-device theorem into unconditional superiority for every memory. No claim in the indifference band or for drift, coherent misalignment or unmodelled errors follows from this test.
