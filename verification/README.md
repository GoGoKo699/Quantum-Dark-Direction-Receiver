# Reproduce the finite comparison

Use Python 3.12 or later with the pinned dependencies in the repository root:

```bash
python -m pip install -r requirements.txt
python verification/run_all.py --output-dir ../dark-direction-checks
```

The output directory is optional and must be outside the source repository. The runner exits on a failed check. No optimizer, numerical SDP solution, private repository or external dataset is required to verify the rational three-specimen certificate.

| Check | What it establishes computationally | Limit |
|---|---|---|
| `check_finite_budget.py` | Exact rational Bayesian moments; two-specimen operator bound; posterior formulas and integrals; nine rational symmetry projectors, stabilizer charges/spins and normalization; positive rational dual and all inequalities | The analytical reduction from every adaptive protocol to the relaxation is explained in the scientific proof. No exact one-copy optimum is claimed. |
| `check_collective_minimax.py` | Exact finite score and hierarchy calculations, including the biseparable and sequential bounds, normalized sector weights and small-system collective risks | The analytic argument gives optimality for arbitrary specimen counts and dimension. |
| `check_calibration.py` | Exact integer/Fraction Chernoff and risk inequalities at the stated total budget, including the receiver-error extension | The binomial, independence, stationarity and uniform control-error models are assumptions. The test does not validate them. |
| `check_implementation.py` | MUB completeness, explicit isometry/unitary completions, Givens reconstruction, posterior score, finite-bit coupling constants and selected matrix examples | Numerical quantile/polar examples illustrate the certified algorithm in the proof. They do not calibrate actual hardware. |
| `check_global_bounds.py` | Intrinsic Fisher normalization for selected random POVMs; coarse-graining; measure-and-prepare channel identity; coherent exchange ambiguity | Sampling POVMs is not the proof of an all-protocol lower bound. |
| `check_receiver.py` | Projective moments through degree four, full nine-dimensional Born probabilities, noisy matrix moments and finite-risk evaluations | Its Monte Carlo comparisons use one selected one-copy estimator, rather than the full adaptive comparator. |

The saved [exploratory numerical reference](receiver_reference_results.json) has a fixed seed and labels the selected baseline. It is not evidence of superiority over every adaptive measurement. That conclusion uses the exact certificate or the global analytical lower bound together with the finite upper bound.

All mathematical statements retain the source, reference-preparation and receiver promises in [the model](../science/model.md). A passing check is not an experiment, independent expert certification, exhaustive novelty verification or hosted rendering review.

## Actual hosted mathematics

The read-only `Hosted mathematics` workflow runs the pinned-source collector on same-repository pull requests. It first probes the README, then compares every Markdown page and every mathematical expression against the actual commit-pinned GitHub renderer at widths 1440 and 760. The artifact retains HTML, screenshots, source/structure comparisons and the report. Human inspection of the actual images remains necessary; a green structural report does not prove visual readability or mathematical correctness.

The included collector/checker bytes come from Guinevere commit `4f63125dafba0e0af2432528627b9cbf56d4b08f`. They execute with an anonymous browser and read-only repository permissions, without a secret or persisted checkout credential. Temporary CI artifacts are verification evidence with limited retention, not a scientific data archive.
