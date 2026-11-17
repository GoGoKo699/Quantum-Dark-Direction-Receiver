# Related work and scientific provenance

The question here is deliberately narrower than general quantum tomography: independent qutrits have the promised state $`\rho_f=(I-|f\rangle\langle f|)/2`$, the missing ray $`f\in\mathbb{CP}^2`$ is wholly unknown, and the output is scored by worst-case expected **dark-ray infidelity**. The known laboratory reference, exact rank, and equal occupied populations are assumptions. The [model](../science/model.md) fixes the comparator and the resource ledger.

## What is inherited and what is proved here

| Ingredient or result | Antecedent | Role in this repository |
|---|---|---|
| Covariant quantum estimation and reduction by symmetry | Holevo [H11]; Keyl [K06] | Established statistical framework; common random rotation turns the relevant average-risk calculation into a uniform risk statement. |
| Symmetric tensor-square effects and antisymmetric effects on a pair | Keyl [K06]; Zhu–Hayashi [ZH18] | Established measurement architecture. The qutrit wedge identifies the conjugate missing ray; neither coherent pair readout nor its physical principle is claimed as new. |
| Unbiased matrix statistics for bounded-copy tomography | Pelecanos–Spilecki–Wright [PSW25] | The large-budget construction uses the two-copy specialization of established Keyl/debiasing ideas. The project supplies its finite dark-ray risk and noise accounting. |
| Separable/PPT optimization for estimation fidelity | Navascués [N08] | Established relaxation method. The explicit finite dark-ray certificate and its rational verification are supplied here. |
| Exact two-specimen equality | [Finite-budget theorem](../science/finite-budget.md) | The optimum risk is $`23/40`$ for both arbitrary collective measurements and adaptive one-copy measurements. It rules out a two-specimen advantage in this model. |
| A strict advantage with three specimens | [Finite-budget theorem](../science/finite-budget.md) | An explicit pair-plus-single receiver beats a certified lower risk bound for **every** adaptive one-copy protocol. The lower bound need not equal that comparator's optimum; no optimality of the three-specimen receiver is claimed. |
| Imperfect storage and paid scalar calibration | [Memory noise](../science/memory-noise.md), [calibration](../science/calibration.md) | Finite guarantees charge signal and reference specimens and calibration failures under the stated depolarizing-memory model. They do not certify arbitrary apparatus errors. |

The finite theorem is not inferred from an asymptotic Fisher-information inequality. Its small-budget comparison uses the complete likelihood and a finite fidelity certificate; its large-budget comparison uses an explicit global estimator and finite upper and lower risk bounds. The [implementation](../science/implementation.md) charges the finite control approximation and the [limits](../science/limits.md) distinguish additional coherent memory from a classical record.

## Closest external comparisons

**Zhu–Hayashi [ZH18].** Projective designs yield efficient two-copy measurements, including universal Fisher symmetry for qubits. Their main two-copy trace theorem is stated for the full-rank full state model. It does not directly give the present rank-two four-parameter orbit's finite minimax risk. The symmetric/antisymmetric construction is an ancestor, not a new contribution of this repository.

**Keyl and debiased Keyl tomography [K06, PSW25].** These sources establish covariant state estimation and unbiased matrix estimators with useful second moments and bounded-copy applications. Our source promise and ray loss allow a specific finite analysis. Recasting their apparatus or matrix estimator alone would not establish a new receiver advantage.

**Nayak–Zhou [NZ26].** Their Theorems 1.1–1.2 determine low-rank trace-norm tomography complexity up to universal constants with adaptive bounded-size joint measurements. Their lower-bound method already combines uniform-spectrum support rotations, Fisher information, adaptive accumulation, and van Trees. Those general ideas are credited. Their order bounds do not identify the exact two-specimen tie, the three-specimen strict gap, or a calibrated receiver's finite risk in the present task.

**Navascués [N08].** A pure target may be encoded in another quantum state, and estimation can be optimized through separable measure-and-prepare operators. Local estimation admits separability/PPT-extension upper bounds on fidelity. This is the direct methodological ancestor of the present finite converse. The new object is the concrete dark-ray instance and verified certificate, not a new SDP framework.

**Yi et al. [Y25].** Their exact three-copy problem concerns Haar-random pure qubits and the distinction between biseparable and genuine three-copy measurements, including the order of pair and single measurements. It is a close precedent for finite measurement-resource hierarchies. Its source family, dimension, and principal comparator differ from the present rank-two qutrit problem. We make no claim to the first three-copy estimation separation in general.

**Hou et al. [Hou18].** A five-outcome collective SIC was implemented deterministically with photonic quantum walks, with finite-sample tomography and apparatus characterization. Their two qubits were encoded in two degrees of freedom of one photon. That experiment is an important implementation precedent; joining two separately emitted unknown specimens still needs the storage/interface resources stated here.

**Conlon et al. [C23].** Explicit single- and two-copy circuits estimated two small noncommuting qubit rotations on noisy platforms, with calibrated error mitigation and observed performance beyond a single-copy precision bound. This already demonstrates experimentally useful noisy collective sensing. Its local model and precision benchmark do not supply a global finite-budget minimax theorem for a wholly unknown qutrit missing ray.

**Antisymmetrization and entanglement-breaking memory [BW26, HSR03].** Preparing an occupied-eigenvector wedge from mixed-state copies is an established primitive. The measure-and-prepare characterization of entanglement-breaking channels is also established. The low-visibility obstruction in [limits](../science/limits.md) is their application to this receiver access model, rather than a new channel characterization.

## Internal source boundary

These repositories were inspected as read-only scientific sources. Their results are credited once; this repository does not modify or replace them.

| Source at the inspected revision | Inherited content | Boundary |
|---|---|---|
| [Calibrated Quantum Readout](https://github.com/GoGoKo699/Calibrated-Quantum-Readout/tree/d78e32a44cd99de01d00e38e8d65d0ddfc0e908b) | Calibrated one-copy information construction, support-rotation converse, complete-record and paid-calibration reasoning | Its full fixed-rank local Fisher objective differs from the present restricted source and global finite ray loss. |
| [Quantum Readout Rank Threshold](https://github.com/GoGoKo699/Quantum-Readout-Rank-Threshold/tree/7be2f7b2cf400425ea236c0feef4617e2ba7534f) | State-independent parity/design readout, pure antisymmetric support encoding, separate continuous-Haar comparison | Its universal rank-two information guarantee and rank-three obstruction are not finite dark-ray risk dominance. |
| [Off the Wall: unknown dark mode](https://github.com/GoGoKo699/Quantum-Off-the-Wall/blob/f9216cb24ba27183dcffa8fd45cce31fe89827a4/science/sensing-applications.md#1-calibrating-an-unknown-dark-mode) | Exact equal-population source, fixed 24-outcome construction, uniform asymptotic coefficient at most $`7.70424`$ versus one-copy lower coefficient $`8`$ | The certificate is not an optimum or a finite-sample guarantee. The present theorem resolves finite instances under explicit additional receiver models. |

## Scope of the comparison

The literature check covered known-spectrum and support estimation, covariant estimation, local/separable/PPT estimation, bounded-copy tomography, and experimental collective sensing. No inspected source states the complete model-specific two-specimen equality and three-specimen advantage proved here. This is a scoped comparison, not a proof of exhaustive priority.

The paid calibration theorem estimates a scalar storage visibility **assuming the isotropic channel law**. It neither validates that law nor learns an unknown laboratory frame or all control errors. Fixed control-error bounds and trusted reference preparation are separate assumptions. Specimen gains are not claims of lower laboratory time, energy, or hardware cost.

## Sources

The keys below match [references.bib](references.bib). Versions and read scope are recorded in [source evidence](SOURCE_EVIDENCE.md).

- **[H11]** A. S. Holevo, *Probabilistic and Statistical Aspects of Quantum Theory* (2011), [publisher](https://doi.org/10.1007/978-88-7642-378-9).
- **[K06]** M. Keyl, *Quantum state estimation and large deviations*, Rev. Math. Phys. **18**, 19–60 (2006), [arXiv](https://arxiv.org/abs/quant-ph/0412053v2).
- **[ZH18]** H. Zhu and M. Hayashi, PRL **120**, 030404 (2018), [arXiv](https://arxiv.org/abs/1709.06112v2).
- **[PSW25]** A. Pelecanos, J. Spilecki and J. Wright, *The debiased Keyl's algorithm* (2025 preprint; STOC 2026), [arXiv](https://arxiv.org/abs/2510.07788v1).
- **[NZ26]** A. Nayak and X. Zhou, *Optimal Low-Rank Quantum State Tomography with Bounded-Sample Joint Measurements* (2026), [arXiv](https://arxiv.org/abs/2609.10514v2).
- **[N08]** M. Navascués, PRL **100**, 070503 (2008), [arXiv](https://arxiv.org/abs/0707.4398v2).
- **[Y25]** C. Yi et al., PRA **111**, 062409 (2025), [arXiv](https://arxiv.org/abs/2412.03383v2).
- **[Hou18]** Z. Hou et al., Nat. Commun. **9**, 1414 (2018), [arXiv](https://arxiv.org/abs/1710.10045v2).
- **[C23]** L. O. Conlon et al., Nat. Phys. **19**, 351–357 (2023), [arXiv](https://arxiv.org/abs/2205.15358v2).
- **[BW26]** A. Bene Watts et al., *Anti-symmetrization is cheap and useful* (2026), [arXiv](https://arxiv.org/abs/2610.06737v1).
- **[HSR03]** M. Horodecki, P. W. Shor and M. B. Ruskai, Rev. Math. Phys. **15**, 629–641 (2003), [arXiv](https://arxiv.org/abs/quant-ph/0302031v2).
- **[GM00]** R. D. Gill and S. Massar, PRA **61**, 042312 (2000), [arXiv](https://arxiv.org/abs/quant-ph/9902063).
- **[ZC26]** S. Zhou and S. Chen, PRX Quantum **7**, 010314 (2026), [publication](https://doi.org/10.1103/s27y-gbrp).
- **[DDG20]** R. Demkowicz-Dobrzański, W. Górecki and M. Guţă, J. Phys. A **53**, 363001 (2020), [arXiv](https://arxiv.org/abs/2001.11742v2).

