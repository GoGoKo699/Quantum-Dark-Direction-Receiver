#!/usr/bin/env python3
"""Exact finite certificate for paid first-qutrit memory calibration.

No sampling, Gaussian approximation, fitted receiver parameter or external
dependency is used. Decimal values are presentation only; strict certificate
inequalities below use integers and fractions.
"""

from decimal import Decimal, localcontext
from fractions import Fraction as F
import json


def dec(value: F) -> Decimal:
    return Decimal(value.numerator) / Decimal(value.denominator)


def check() -> dict:
    calibration_pairs = 100_000
    signal_pairs = 1_400_000
    total_specimens = 2 * (calibration_pairs + signal_pairs)
    cutoff = 500
    q = F(1, 200)
    nu_good = F(99, 100)
    nu_signal_bound = F(49, 50)
    t = F(1, 80)
    assert cutoff == calibration_pairs * q

    # Born-rule parity probability for D_nu(P0) tensor P0.
    for nu in (F(0), nu_signal_bound, nu_good, F(1)):
        swap_expectation = nu + (1 - nu) / 3
        parity_probability = (1 - swap_expectation) / 2
        assert parity_probability == (1 - nu) / 3
    assert (1 - nu_good) / 3 == F(1, 300)
    assert (1 - nu_signal_bound) / 3 == F(1, 150)

    # exp[-M D_Ber(q || p)] has an exact rational expression because Mq
    # is an integer. Rejection is A>=501; the A>=500 upper-tail bound
    # is conservative. Acceptance is A<=500.
    alpha_num = 2**500 * 598**99_500
    alpha_den = 3**500 * 597**99_500
    beta_num = 4**500 * 596**99_500
    beta_den = 3**500 * 597**99_500
    assert alpha_num * 10**15 < alpha_den
    assert beta_num * 10**11 < 11 * beta_den

    # Fallback is uniformly one of the three computational rays: its
    # expected overlap is (1/3)sum_j |<j|f>|^2 = 1/3 for every f.
    fallback_risk = F(2, 3)
    gap_bound = (1 + nu_signal_bound) / 2
    tangent_variance_bound = (103 - 4 * nu_signal_bound) / 30
    assert 0 < t < gap_bound / 2
    moment_term = tangent_variance_bound / (
        signal_pairs * (gap_bound - 2 * t) ** 2
    )
    exponent = signal_pairs * t**2 / (F(21, 2) + F(8, 3) * t)
    assert moment_term == F(2477, 977_786_250)
    assert exponent == F(13125, 632)

    # e^-x <= (1+x/1000)^-1000, an exact rational upper bound.
    tail_upper = 6 * (1 + exponent / 1000) ** (-1000)
    assert tail_upper == 6 * F(5056, 5161) ** 1000
    alpha_upper = F(1, 10**15)
    certified_risk_upper = moment_term + tail_upper + fallback_risk * alpha_upper

    # sqrt[B(B+16)] <= B+8 gives L_B >= 8/(B+16).
    comparator_lower_relaxation = F(8, total_specimens + 16)
    assert certified_risk_upper < comparator_lower_relaxation
    assert certified_risk_upper < F(2541, 10**9)
    assert comparator_lower_relaxation > F(2666, 10**9)

    # Additional independently certified receiver/control errors: each full
    # pair-outcome distribution is within TV tau of the D_nu model. The
    # calibration test does not infer or certify this uniform tau promise.
    tau = F(1, 100_000)
    robust_t = F(9, 500)
    robust_good_endpoint = F(1, 300) + tau
    robust_bad_endpoint = F(1, 150) - tau
    assert robust_good_endpoint == F(1003, 300_000) < q
    assert robust_bad_endpoint == F(1997, 300_000) > q
    robust_alpha_num = 1003**500 * 298997**99_500
    robust_alpha_den = 1500**500 * 298500**99_500
    robust_beta_num = 1997**500 * 298003**99_500
    robust_beta_den = 1500**500 * 298500**99_500
    assert robust_alpha_num * 10**15 < robust_alpha_den
    assert robust_beta_num * 10**11 < 14 * robust_beta_den
    robust_gap = gap_bound - 2 * robust_t - 12 * tau
    assert robust_gap > 0
    robust_moment_bias = (
        (tangent_variance_bound + 9 * tau) / signal_pairs + 36 * tau**2
    ) / robust_gap**2
    robust_exponent = signal_pairs * robust_t**2 / (18 + 4 * robust_t)
    assert robust_moment_bias == F(992339, 382_152_562_848)
    assert robust_exponent == F(6300, 251)
    robust_tail_upper = 6 * (1 + robust_exponent / 1000) ** (-1000)
    assert robust_tail_upper == 6 * F(2510, 2573) ** 1000
    robust_certified_risk_upper = (
        robust_moment_bias + robust_tail_upper + fallback_risk * alpha_upper
    )
    assert robust_certified_risk_upper < comparator_lower_relaxation
    assert robust_certified_risk_upper < F(2597, 10**9)

    with localcontext() as context:
        context.prec = 70
        alpha = Decimal(alpha_num) / Decimal(alpha_den)
        beta = Decimal(beta_num) / Decimal(beta_den)
        risk_upper = (
            dec(moment_term)
            + 6 * (-dec(exponent)).exp()
            + dec(fallback_risk) * alpha
        )
        b = Decimal(total_specimens)
        comparator_lower = 16 / (b + 24 + (b * (b + 16)).sqrt())
        robust_alpha = Decimal(robust_alpha_num) / Decimal(robust_alpha_den)
        robust_beta = Decimal(robust_beta_num) / Decimal(robust_beta_den)
        robust_risk_upper = (
            dec(robust_moment_bias)
            + 6 * (-dec(robust_exponent)).exp()
            + dec(fallback_risk) * robust_alpha
        )
        return {
            "status": "passed",
            "model": "independent stationary D_nu on first stored qutrit only",
            "performance_range": "nu >= 99/100",
            "signal_bound_uses": "nu >= 49/50",
            "calibration_pairs": calibration_pairs,
            "signal_pairs": signal_pairs,
            "total_specimens": total_specimens,
            "acceptance": "antisymmetric calibration count <= 500",
            "alpha_chernoff_bound": str(alpha),
            "beta_chernoff_bound": str(beta),
            "signal_plus_fallback_risk_upper": str(risk_upper),
            "rational_certified_risk_upper": str(dec(certified_risk_upper)),
            "all_adaptive_one_copy_risk_lower": str(comparator_lower),
            "strict_rational_certificate": True,
            "beta_is_separate_soundness_bound": True,
            "all_signal_specimens_measured_on_reject": True,
            "bounded_receiver_error_extension": {
                "externally_certified_outcome_tv_bound": str(tau),
                "calibration_does_not_learn_tv_bound": True,
                "alpha_chernoff_bound": str(robust_alpha),
                "beta_chernoff_bound": str(robust_beta),
                "risk_upper": str(robust_risk_upper),
                "rational_certified_risk_upper": str(
                    dec(robust_certified_risk_upper)
                ),
                "strict_rational_certificate": True,
            },
        }


if __name__ == "__main__":
    print(json.dumps(check(), indent=2))
