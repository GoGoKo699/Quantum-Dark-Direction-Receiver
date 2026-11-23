# Learn the dark-ray estimation story

A source leaves one direction empty. The receiver must report that unknown ray from independently supplied specimens. Follow a [worked qutrit example](STORY.md) from the pair readout to the exact three-specimen hierarchy, then see what changes when the same device needs paid memory calibration.

The single educational anchor is Demkowicz-Dobrzański, Górecki and Guţă's 2020 review, [*Multi-parameter estimation beyond Quantum Fisher Information*](https://arxiv.org/abs/2001.11742v2). The [anchor bridge](ANCHOR.md) translates the review's conventions into this experiment and points to the additional proofs.

## Follow the 30 milestones

| Milestones | Understanding target | Scientific destination |
|---|---|---|
| M01–M12 | State one fair experiment in terms of source, loss, access, budget and symmetry. | [Model](../science/model.md) |
| M13–M19 | Work through the qutrit pair readout, derive the exact collective score, and see when shared access first helps. | [Pair receiver](../science/receiver.md), [collective minimax](../science/collective-minimax.md) and [measurement hierarchy](../science/measurement-hierarchy.md) |
| M20–M22 | Distinguish exact finite outcome designs from physical implementation with bounded control errors. | [Collective POVM](../science/collective-minimax.md) and [pair implementation](../science/implementation.md) |
| M23–M28 | Audit the noisy pair estimator, its reference test and the total-risk ledger. | [Memory noise](../science/memory-noise.md) and [paid calibration](../science/calibration.md) |
| M29–M30 | Connect the ideal result and the calibrated experiment, including the assumptions behind each. | [Limits](../science/limits.md) and [prior work](../references/RELATED_WORK.md) |

The [milestone map](MILESTONES.md) gives twelve background targets and eighteen narrative targets. The background closes with one complete decision problem. The narrative follows it from exact ideal risks to the explicit resources needed for a noisy receiver. The [scientific route](../science/README.md) leads directly to the proofs. The [verification guide](../verification/README.md) identifies the identities and numerical bounds checked in code.
