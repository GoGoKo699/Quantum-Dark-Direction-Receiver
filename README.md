# Quantum Dark Direction Receiver

**How many specimens must a receiver measure together to locate an unknown empty direction?** Each independent specimen occupies the orthogonal complement of an unknown ray $`f`$ with equal populations. The receiver estimates $`f`$ in a known laboratory reference and minimizes worst-case expected ray infidelity.

For any dimension and specimen budget, the [collective minimax theorem](science/collective-minimax.md) gives the exact risk and a finite measurement attaining it. In dimension $`d\ge3`$, separate measurements are optimal through $`d-1`$ specimens. At $`d`$ specimens, attaining the optimum requires a measurement across all $`d`$.

## Three qutrits

Two qutrits give exact risk $`23/40`$ with either separate or collective measurements. At three specimens the [measurement hierarchy](science/measurement-hierarchy.md) gives four distinct levels.

| Measurement access | Minimax infidelity |
|---|---:|
| Fully joint | $`21/40=0.525`$, exact |
| Individual POVM effects biseparable across possibly different cuts | $`1-25/64-\sqrt{6001}/960\approx0.52868112`$, exact |
| Fixed-cut separable or sequential joint pair and single in either order | $`1-83/192-3\sqrt{17}/320\approx0.52905422`$, exact |
| Adaptive single-copy | $`\ge 0.53735011`$, certified lower bound |

The broad class with biseparable effects allows different bipartitions across effects of one measurement. Randomizing over complete fixed-cut separable measurements gives the fixed-cut value. The converse uses the fully antisymmetric sector. The source never occupies that sector, but the complete measurement still has to cover it.

## Finite control and paid calibration

The [finite implementation](science/implementation.md) gives a three-specimen pair receiver with bounded control error and risk below $`0.531375`$. It uses a 24-outcome pair measurement, a 12-outcome single measurement and 2304 fair random bits. The receiver stores one qutrit before joining the second.

The [paid-calibration result](science/calibration.md) uses a separate fixed 450-outcome pair receiver and global matrix estimator. At a total budget of three million, including 200,000 known-reference specimens, its risk is below $`2.596812\times10^{-6}`$. Even with the entire budget as signals and ideal apparatus, adaptive single-copy readout has risk above $`2.666652\times10^{-6}`$. The analysis assumes independent stationary first-qutrit depolarizing storage with visibility at least $`0.99`$ and a separate full-outcome readout-error bound of $`10^{-5}`$ in total variation. Calibration rejection contributes to unconditional risk. An unknown coherent rotation can make the parity architecture ambiguous. See [receiver limits](science/limits.md).

## Read the science

Start with the [scientific route](science/README.md) or [model and resource ledger](science/model.md). The [source comparison](references/RELATED_WORK.md) credits the inherited Keyl receiver, two-copy readout and matrix estimator. The new results are the exact finite ray-loss converse and the comparison between measurement classes. The collective theorem concerns ideal measurement access and specimen counts. The finite pair implementation has its own control promises and calibration ledger.

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
