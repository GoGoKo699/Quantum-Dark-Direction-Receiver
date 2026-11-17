# A finite lower bound for every adaptive one-copy receiver

The small-budget [PPT certificate](finite-budget.md) gives the useful three-specimen converse. For larger budgets, a geometric integration identity supplies a simple explicit lower bound, including biased estimators and complete adaptive records. The information tradeoff and Bayesian integration methods are established tools; their normalization and finite dark-ray consequence are given here.

## Statement

For the [promised source and ray loss](model.md), every adaptive one-copy protocol using at most $`N`$ signal specimens satisfies

```math
\boxed{
R_N\ge L_N:=\frac{16}{N+24+\sqrt{N(N+16)}}.
}
```

The bound is global and finite. At $`N=0`$ it gives the exact no-data risk $`2/3`$. Its coefficient tends to eight, but the finite expression, rather than that limit, is used in the noisy and paid-calibration comparisons. It is not the exact finite one-copy optimum.

## One-copy information budget

Use the Fubini–Study metric for which a tangent $`\delta\perp f`$ has squared norm $`\|\delta\|^2`$ and infidelity has the same leading quadratic term. Refine a POVM to rank-one effects $`w(y)P_{\psi_y}`$. Put $`u_y=\mathrm{tr}(P_{\psi_y}P_f)`$. Then

```math
p_y=\frac{w(y)}2(1-u_y),\qquad
\|\nabla u_y\|^2=4u_y(1-u_y),\qquad
\frac{\|\nabla p_y\|^2}{p_y}=2w(y)u_y.
```

Completeness integrates the final expression to two. Coarse-graining cannot increase Fisher information, so every one-copy POVM has intrinsic Fisher trace at most two. A fresh ancilla induces an ordinary POVM and changes nothing. At zero probability, the ordinary score convention omits a zero derivative contribution; this can only lower the bound.

For adaptation, condition on the complete earlier classical record. The next setting is then held fixed when differentiating its Born probability. Score increments have conditional mean zero, so their cross terms vanish and

```math
\mathrm{tr}_g I_{\mathrm{record}}(f)\le2N.
```

All pilots, setting randomization and final estimator randomization belong to that record. A hard-cap stopping rule obeys the same inequality. General outcome spaces admit a parameter-independent dominating trace measure and sequential kernels; finiteness of the outcome alphabet is unnecessary.

## Haar integration without localization

Give $`f`$ the normalized Haar prior on $`\mathbb{CP}^2`$. For fixed complete record $`y`$, let $`H_y=P_{\widehat f(y)}`$ and $`q_y(f)=\mathrm{tr}(H_yP_f)`$. The intrinsic identities are

```math
\Delta q_y=-12(q_y-1/3),\qquad
\|\nabla q_y\|^2=4q_y(1-q_y).
```

For normalization, at $`f=e_0`$ use local coordinates $`f(z)=(\sqrt{1-|z|^2},z_1,z_2)`$. The sum of its four real second derivatives of $`q`$ is $`4[1-3q]`$; unitary invariance gives the Laplacian everywhere.

The manifold is compact without boundary. Integrating $`p_y\Delta q_y`$ by parts and then over records, with Haar Bayes risk $`R=\mathbb E(1-q)`$, gives

```math
12(2/3-R)=\mathbb E\langle\nabla q,s\rangle,
\qquad s=\nabla\log p_y.
```

The identity can be expressed using $`\nabla p_y`$ before dividing by the likelihood, so zero-density points do not create an uncharged regularity assumption. Conditional Born likelihoods are smooth for each fixed record.

Cauchy–Schwarz, the information budget and Jensen's inequality imply

```math
\begin{aligned}
144(2/3-R)^2
&\le(2N)\,4\mathbb E[q(1-q)]\\
&\le8NR(1-R),\\
(N+18)R^2-(N+24)R+8&\le0.
\end{aligned}
```

The smaller root is the boxed expression. Worst-case risk is at least Haar average risk for each protocol, proving the minimax lower bound without an unbiasedness premise or a supplied local chart.

## Calibration in the comparator

Known-reference preparations independent of $`f`$ do not add dark-ray information. With a total specimen budget $`B`$, granting the comparator $`B`$ informative signals and ideal apparatus strengthens it. The [paid pair receiver](calibration.md) is compared to $`L_B`$ under precisely that stronger grant. Calibration that itself carries unknown-ray information would require its actual signal likelihood and cannot be replaced by this argument.
