# A global finite-risk receiver with imperfect storage

The pair receiver can tolerate imperfect storage without first localizing the unknown ray. This page proves a finite inequality for its globally defined matrix estimator. The memory family and its independence assumptions are part of the theorem.

## Physical memory model

The first specimen waits for the second through

```math
\mathcal D_\nu(T)=\nu T+(1-\nu)\operatorname{tr}(T)I/3,
\qquad 0\le\nu\le1.
```

The second specimen is fresh. Uses are independent conditional on the fixed unknown $`\nu`$. The signal pair is $`\mathcal D_\nu(\rho_f)\otimes\rho_f`$. This differs from depolarizing the whole pair. The readout is the fixed 450-outcome [design receiver](receiver.md), retaining both branches.

Put $`u_\ell=\operatorname{tr}(P_{\psi_\ell}P_f)`$. Direct Born probabilities are

```math
\begin{aligned}
p_\ell^+&=w_\ell\left[\frac{3\nu}{2}(1-u_\ell)^2
 +(1-\nu)(1-u_\ell)\right],\\
p_\ell^-&=w_\ell\left[\frac{1-\nu}{4}
 +\frac{2\nu+1}{4}u_\ell\right].
\end{aligned}
```

In particular $`p_-=(4-\nu)/12`$. The complete signal parity record can estimate $`\nu`$; no plug-in estimate enters the ray estimator below. The [paid-reference theorem](calibration.md) uses a more informative known input to certify an operating range.

## Exact moments

Write $`P=P_f`$, $`b=(1+\nu)/2`$ and $`c=(1-\nu)/6`$. For the score matrix $`Z`$ in [the receiver](receiver.md), the 4-design identities imply

```math
\begin{aligned}
\mathbb EZ&=bP+cI,\\
V(\nu):=\mathbb E\|(I-P)Zf\|^2&=\frac{103-4\nu}{30},\\
\mathbb E(Z-\mathbb EZ)^2
&=\frac{182+8\nu-\nu^2}{36}I
 -\frac{8+6\nu+\nu^2}{12}P.
\end{aligned}
```

One way to verify the algebra is to use the branch first moments

```math
\begin{aligned}
\mathbb E[1_+P_\psi]&=\frac{5+\nu}{20}I-\frac{5+4\nu}{60}P,\\
\mathbb E[1_-P_\psi]&=\frac{5-2\nu}{48}I+\frac{1+2\nu}{48}P,
\end{aligned}
```

and the tangent moments $`\mathbb E[1_+u(1-u)]=1/10`$ and $`\mathbb E[1_-u(1-u)]=(7-\nu)/120`$. Uniformly over $`0\le\nu\le1`$,

```math
\|Z-\mathbb EZ\|\le4,\qquad
\|\mathbb E(Z-\mathbb EZ)^2\|\le\frac{21}{4}.
```

The mean gap $`b`$ is at least $`1/2`$, and its principal eigenray is always $`f`$. This is why unknown visibility does not require a preliminary fitted likelihood.

## Finite risk, including large errors

Let $`H=K^{-1}\sum_{j=1}^K Z_j`$ and output its leading eigenray. For every $`0<t<b/2`$,

```math
\boxed{
\sup_f\mathbb E_f\ell(\widehat f,f)
\le U(K,\nu,t):=
\frac{103-4\nu}{30K((1+\nu)/2-2t)^2}
+6\exp\left[-\frac{Kt^2}{21/2+8t/3}\right].
}
```

To prove this, put $`E=H-\mathbb EH`$. Hermitian matrix Bernstein gives

```math
\Pr(\|E\|>t)\le6\exp[-Kt^2/(21/2+8t/3)].
```

On $`\|E\|\le t`$, let $`\widehat f=\alpha f+v`$, $`v\perp f`$. The leading eigenvalue is at least $`b+c-t`$. Projecting its eigen-equation onto $`f^\perp`$ gives

```math
\|v\|^2\le\frac{\|(I-P)Ef\|^2}{(b-2t)^2}.
```

Independence and zero mean imply $`\mathbb E\|(I-P)Ef\|^2=V(\nu)/K`$. On the remaining event, use loss at most one. This proves the boxed bound without conditioning away a failed localization or ignoring rare large errors. The estimator has no localization pilot. Since $`V`$ decreases and $`b`$ increases in $`\nu`$, substituting a declared lower bound $`\nu_0`$ gives a uniform nuisance-range theorem.

## A strict finite comparison

Every adaptive one-copy protocol with $`N`$ specimens satisfies the [global lower bound](one-copy-bound.md)

```math
L_N=\frac{16}{N+24+\sqrt{N(N+16)}}.
```

For $`\nu\ge9/10`$, set $`t=3/200`$. The receiver bound simplifies to

```math
R_{2K}\le\frac{12425}{3174K}+6e^{-9K/421600}.
```

At $`K=10^6`$ this is below $`L_{2K}`$. A simple exact check uses $`L_{2K}\ge4/(K+8)`$ and an elementary rational upper bound on the exponential. For every larger $`K`$, $`Ke^{-9K/421600}`$ decreases while $`4K/(K+8)`$ increases. Hence the strict comparison holds for **every even $`N\ge2{,}000{,}000`$**, uniformly over all rays and $`\nu\ge0.9`$. These conservative sufficient budgets are not optimal experimental crossover estimates.

## Bounded additional readout errors

An explicit implementation tolerance can be included without multiplying a per-pair error by all pairs. Suppose each complete pair outcome distribution differs from the ideal noisy-memory distribution by total variation at most $`\tau`$, uniformly over $`f`$, and the resulting samples remain independent. Extend the ideal distribution by zero probabilities for any padded dilation labels, assign those actual labels matrix score zero and recode their parity as plus; they remain in the record. This is an extra declared readout/control contract; a scalar parity test does not establish it.

Because $`\|Z\|\le3`$, the mean perturbation obeys $`\|\Delta\|\le6\tau`$. Also $`\|(I-P)Zf\|^2\le25/4`$, so its second moment increases by at most $`25\tau/4`$. Centering at the actual mean gives sample norm at most six and variance norm at most nine. Thus for $`b-2t-12\tau>0`$,

```math
R\le
\frac{(V(\nu)+25\tau/4)/K+36\tau^2}
 {(b-2t-12\tau)^2}
+6\exp[-Kt^2/(18+4t)].
```

For the numerator, the centered sample average and the deterministic mean perturbation have zero cross term in expectation. The same projected eigen-equation applies with total operator deviation at most $`t+6\tau`$. This includes systematic bias and all concentration failures. It exposes a bias floor of order $`\tau^2`$; fixed arbitrary errors cannot be claimed harmless at unlimited precision. [Calibration](calibration.md) states a finite total-budget tolerance and shifts the binomial endpoints consistently.
