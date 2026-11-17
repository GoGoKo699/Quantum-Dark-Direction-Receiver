# A missing qutrit direction as an estimation task

A source fills a two-dimensional subspace equally and leaves its orthogonal ray empty. The receiver must identify that missing ray in a known laboratory reference. This is a promised state-estimation experiment, rather than a model of every physical device with a weak or dark response.

## Input, output and loss

For a wholly unknown ray $`f\in\mathbb{CP}^2`$, every independent signal specimen has state

```math
\rho_f=\frac{I-P_f}{2},\qquad P_f=|f\rangle\!\langle f|.
```

The occupied eigenvalues are exactly $`1/2,1/2`$, and the third eigenvalue is exactly zero. No nominal ray, eigenspace, preliminary localization or training example of $`f`$ is supplied. The laboratory qutrit basis and the declared control model are known. Changing the population promise, allowing full-rank leakage or removing that reference changes the experiment.

The output is a ray $`\widehat f`$. Its loss and a protocol's risk are

```math
\ell(\widehat f,f)=1-\operatorname{tr}(P_{\widehat f}P_f),
\qquad
R(\mathsf P)=\sup_f\mathbb E_f\ell(\widehat f,f).
```

This is dark-ray infidelity, not mixed-state infidelity of two preparations. The expectation includes measurement outcomes, settings, classical randomization, calibration and fallback events.

## Measurement classes

The **one-copy comparator** may measure every fresh specimen with an arbitrary POVM, use fresh parameter-independent ancillas, retain its complete classical history, change every subsequent measurement adaptively, and output any biased or randomized estimate. No coherent system may connect two unknown specimens. All signal pilots count. This permits much more than a fixed laboratory basis or a chosen tomography algorithm.

The **pair receiver** may store one qutrit for one preparation interval and measure it jointly with a fresh second qutrit. Between blocks it retains classical data. An odd remaining specimen can be measured separately. All parity branches and all readout outcomes count; antisymmetric heralding does not supply free successful specimens.

For the finite three-specimen theorem, controls are known and ideal until the explicitly quantified implementation perturbation is introduced. For the larger-budget theorem, the first qutrit passes through a specified memory channel and the pair readout has a declared error contract. These are different operating points of the same target task.

## Total specimen accounting

With $`K`$ signal pairs and $`M`$ independent known-reference pairs, the total budget is

```math
B=2K+2M.
```

Both reference qutrits count even though their preparation is known. Reference preparation is a physical resource and must obey the stated reference promise. To make the comparison conservative, the lower bound grants the one-copy comparator **all $`B`$ specimens as unknown-source signals and ideal calibrated apparatus**. An upper bound that beats this stronger comparator establishes a specimen advantage after calibration is charged.

The fixed-budget protocol measures every allocated signal pair even when calibration rejects. Its final fallback is included in the loss. A test's false-acceptance probability is a separate certification statement; it does not make bad hardware disappear from an unconditional risk calculation.

## Results and their domains

| Result | Exact scope | Authoritative proof |
|---|---|---|
| Two specimens give no collective advantage | Global minimax risk $`23/40`$ for unrestricted collective and adaptive one-copy readout | [Finite budgets](finite-budget.md) |
| Three specimens permit a pair advantage | Ideal pair-plus-single risk $`1907/3600`$; every adaptive one-copy risk is at least $`0.53735011`$ | [Finite budgets](finite-budget.md) |
| A finite implementation preserves the small-budget gap | Fixed finite quantum outcomes, finite random settings and explicitly bounded control precision | [Implementation](implementation.md) |
| A fixed 450-outcome receiver tolerates specified memory noise | Global finite risk, with every signal record retained | [Memory noise](memory-noise.md) |
| Independent calibration can be paid | Explicit total budget, stationarity/independence promises and unconditional failure contributions | [Calibration](calibration.md) |
| Some memory errors destroy the construction's benefit | Exact exchange ambiguity for SWAP-commuting readouts; entanglement-breaking simulation for sufficiently depolarized storage | [Limits](limits.md) |

The exact three-specimen one-copy optimum and the optimal pair receiver are not determined. A numerical comparison with selected estimators is reported separately from the class-wide certified bound. Specimen savings do not establish laboratory-time, gate-count, energy or hardware-cost savings.
