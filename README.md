# Quantum Dark Direction Receiver

**When can two-copy readout identify an entirely unknown missing direction better than every adaptive one-copy measurement?** Independent qutrits have state $`\rho_f=(I-|f\rangle\langle f|)/2`$. The target is the wholly unknown ray $`f\in\mathbb{CP}^2`$, scored by worst-case expected ray infidelity. Exact rank two, equal populations and a known laboratory reference are explicit promises.

Two specimens cannot help: even unrestricted collective measurements have the same minimax risk $`23/40`$ as adaptive one-copy readout. **Three specimens suffice.** A pair-plus-single construction has a certified finite advantage over the complete adaptive one-copy class, including biased estimators and all classical histories.

## Finite results

| Operating point | Pair receiver | Every adaptive one-copy receiver |
|---|---|---|
| Two specimens, ideal known controls | Exact risk $`23/40`$ | Exact risk $`23/40`$ |
| Three specimens, covariant ideal benchmark | Risk $`1907/3600\approx0.529722`$ | Risk at least $`0.53735011`$ |
| Three specimens, explicit finite randomness and declared control tolerances | Risk below $`0.531375`$ | Same lower bound $`0.53735011`$ |
| Total budget three million, paid scalar memory calibration and bounded readout errors | Certified risk below $`2.596812\times10^{-6}`$ | Risk above $`2.666652\times10^{-6}`$, even granting all specimens as signals and ideal apparatus |

The [three-specimen converse](science/finite-budget.md) is an exact rational PPT certificate, rather than an asymptotic Fisher comparison or a simulation against selected strategies. The [finite implementation](science/implementation.md) uses a fixed 24-outcome pair measurement, a 12-outcome single measurement, 2304 fair random bits and quantified rotation/readout tolerances. It stores only one qutrit before joining the second.

The [paid-calibration result](science/calibration.md) uses a separate fixed 450-outcome receiver and global matrix estimator. Its three-million-specimen ledger contains 200,000 known-reference specimens and 2.8 million signal specimens. It assumes independent stationary first-qutrit depolarizing storage with visibility at least $`0.99`$ and a separately established full-outcome readout-error bound of $`10^{-5}`$ in total variation. Calibration rejection contributes to unconditional risk. The scalar check does not learn arbitrary control errors or validate the isotropic noise law.

## Read the science

Start with the [scientific route](science/README.md), then choose a question:

| Question | Account |
|---|---|
| What is unknown, and what may the comparator do? | [Model and resource ledger](science/model.md) |
| How does a pair reveal its missing ray? | [Parity, conjugate hole and fixed receivers](science/receiver.md) |
| Why is three the earliest useful total budget? | [Exact finite comparison and certificate](science/finite-budget.md) |
| How are randomness and control precision finite? | [Implementation](science/implementation.md) |
| How are all adaptive one-copy strategies bounded at larger budgets? | [Global lower bound](science/one-copy-bound.md) |
| What survives imperfect storage and paid calibration? | [Memory noise](science/memory-noise.md) and [calibration](science/calibration.md) |
| Which imperfections defeat this architecture? | [Coherent ambiguity and entanglement-breaking limits](science/limits.md) |
| Which results are inherited? | [Related work](references/RELATED_WORK.md) |

## Attribution and practical scope

The two-copy symmetry architecture, Keyl measurement and basic matrix estimator are inherited. Local-estimation/PPT certification and experimental two-copy sensing also have established precedents. The contribution here is the model-specific finite dark-ray separation, its earliest total-budget onset, and the specified noise/calibration resource comparison. The [source comparison](references/RELATED_WORK.md) states these boundaries explicitly.

Unknown coherent memory rotation can make the parity architecture unidentifiable; scalar visibility calibration does not fix that problem. No optimal pair constant, exact three-specimen one-copy optimum, unrestricted hardware-noise theorem, laboratory-time saving or hardware-cost advantage is claimed.

## Learn the complete story

The selected educational anchor is Demkowicz-Dobrzański, Górecki and Guţă, *Multi-parameter estimation beyond Quantum Fisher Information* (2020), [arXiv:2001.11742v2](https://arxiv.org/abs/2001.11742v2). Begin with the [worked story](learning/STORY.md), then the [source-to-project bridge](learning/ANCHOR.md) and the [30-milestone map](learning/MILESTONES.md). The [learning entrypoint](learning/README.md) connects the background, finite receiver and paid-calibration account.

## Reproduce

```bash
python -m pip install -r requirements.txt
python verification/run_all.py --output-dir ../dark-direction-checks
```

The [verification guide](verification/README.md) distinguishes exact rational checks, numerical matrix identities and selected-strategy Monte Carlo comparisons. Source code is covered by the existing [MIT license](LICENSE).

## Purpose and contact

This repository records the scientific account and supports self-directed learning. For discussion or collaboration, contact Ruge Lin at [gogoko699@gmail.com](mailto:gogoko699@gmail.com).
