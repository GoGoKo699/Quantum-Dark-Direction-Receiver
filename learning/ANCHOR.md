# From the 2020 review to this receiver

The single educational anchor is **Rafał Demkowicz-Dobrzański, Wojciech Górecki and Mădălin Guţă, _Multi-parameter estimation beyond Quantum Fisher Information_**, J. Phys. A **53**, 363001 (2020), [arXiv:2001.11742v2](https://arxiv.org/abs/2001.11742v2). The [HTML text](https://arxiv.org/html/2001.11742v2) provides section navigation. Primary papers in [the scientific references](../references/RELATED_WORK.md) remain attribution and proof dependencies, rather than additional educational anchors.

## A focused reading path

| Review section | Read for | Project connection |
|---|---|---|
| §1.2 | Measurement, decision and loss as one experiment | The unknown ray, complete record and worst-case risk |
| §§2.1–2.2 | Classical information versus the SLD benchmark | Angular normalization and limits of local bounds |
| §5.3 | Symmetry, invariant averaging and a measurement seed | Haar averaging and the finite comparator reduction |
| §5.4, especially §5.4.1 | A finite-copy fidelity calculation for qubits | A methodological example, with a different state family and cost normalization |
| §5.5 | Bayesian information bounds and their qualifications | A route toward the project's global lower bound |

The review supplies the estimation framework. The qutrit wedge, MUB receiver, three-specimen PPT certificate, finite control construction, matrix concentration and paid calibration are supplied by the project's scientific account. Reading the review does not establish those results automatically.

## Translate the symbols before comparing constants

The review uses a real parameter vector. Here that vector is only a local description of a ray. Around $`f=e_0`$, choose

```math
f(z)=\left(\sqrt{1-|z_1|^2-|z_2|^2},z_1,z_2\right),
\qquad
z_a=x_a+i y_a.
```

The four real coordinates are $`(x_1,y_1,x_2,y_2)`$. The coordinate chart is a tool for this explanation; the actual task does not supply $`e_0`$ or a preliminary estimate. Every laboratory orientation remains possible.

| Estimation object | In this project |
|---|---|
| Parameterized quantum input | The mixed specimen $`\rho_f=(I-P_f)/2`$ |
| Measurement result | A complete pair or single record, including the branch and known random setting |
| Estimator | The reported ray projector $`\widehat P`$ |
| Cost | $`1-\operatorname{tr}(\widehat P P_f)`$ |
| Worst-case risk | $`\sup_f\mathbb E_f[1-\operatorname{tr}(\widehat P P_f)]`$ |
| Haar Bayes risk | The same expected loss averaged uniformly over rays; useful for a converse and for symmetry |

At the chart origin, infidelity is exactly $`|z_1|^2+|z_2|^2`$ when one ray is $`e_0`$. Its leading quadratic cost matrix is therefore the four-dimensional identity. The review's pure-qubit example in §5.4.1, Eq. (203), instead uses **four times** unscaled ray infidelity. Its numerical cost constants must be rescaled before comparison.

The target projector and the supplied specimen also have different information. With the local squared-length convention above,

```math
J_{P_f}=4I_4,\qquad
J_{\rho_f}=2I_4,\qquad
J_{\rho_f\otimes\rho_f}=4I_4.
```

For example, along $`z_1=x`$, the derivative of the supplied mixed state at zero is $`-(|1\rangle\langle0|+|0\rangle\langle1|)/2`$. Its SLD has the two corresponding off-diagonal entries $`-2`$, and its SLD information is two. The pure target would have information four, but no copy of that target is supplied. Independence doubles the mixed specimen's QFI for a pair; it does not make both inputs pure.

The [one-copy information proof](../science/one-copy-bound.md) bounds the trace of the **classical** information of each one-copy POVM by two in these four angular directions. This differs from the trace eight of its SLD QFI. Neither trace comparison alone is a finite-risk theorem.

## The three transitions supplied here

**From local sensitivity to a global output.** An inverse information matrix is a local covariance benchmark with statistical qualifications. The project's [finite-budget proof](../science/finite-budget.md) instead gives a direct ray decision rule, an exact risk comparison at three specimens and a certificate covering biased adaptive one-copy estimators. The [global lower bound](../science/one-copy-bound.md) uses integration over the entire ray space. No localization success event is discarded.

**From a Haar average to an unknown laboratory direction.** The ray space is the orbit of a reference ray under $`U(3)`$, with stabilizer $`U(1)\times U(2)`$. Unitary conjugation preserves both the source law and ray infidelity. Averaging a complete measurement-and-output rule over a known independent laboratory unitary makes its risk constant. Its Haar-average performance then becomes its worst-case performance. The [finite implementation](../science/implementation.md) additionally pays a uniform error for finite random bits, finite rotations and conditioning fallback; an exact finite Haar sampler is not assumed.

**From a receiver promise to a calibrated operating range.** The [calibration experiment](../science/calibration.md) uses known pure references to check a scalar memory parameter in a declared stationary depolarizing model. All references and rejection events count. It does not learn an arbitrary receiver channel or an unknown coherent frame, and the separate control-error tolerance remains a premise. The [limitations](../science/limits.md) show why this distinction changes identifiability.

## Continue through the project

The [worked story](STORY.md) follows one concrete missing direction through the branches, the output rule and the total budget. The [30-milestone map](MILESTONES.md) then connects the foundations to the finite theorem, implementation, noisy receiver and limits. Specialist proofs remain in [the scientific route](../science/README.md).
