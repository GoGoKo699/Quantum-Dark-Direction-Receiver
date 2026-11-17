#!/usr/bin/env python3
"""Check the finite-budget theorem using exact rational arithmetic.

Requires only Python and SymPy.  No optimizer, NumPy archive, floating SDP
solution, or network resource is used.  The saved certificate is untrusted
input: its positivity, all dual inequalities, and its objective are recomputed.
Run from any working directory: python verification/check_finite_budget.py
"""
from fractions import Fraction
from itertools import product
from math import factorial, prod
from pathlib import Path
import json

import sympy as sp


def require(condition, message):
    if not condition:
        raise ValueError(message)


def haar_moment(alpha):
    """E prod_j |f_j|**(2 alpha_j), f Haar in CP^2."""
    return Fraction(2 * prod(factorial(a) for a in alpha),
                    factorial(sum(alpha) + 2))


def moment_operator(n):
    """B=E[rho_f**tensor(n) |f_0|^2], constructed from integer moments."""
    words = list(product(range(3), repeat=n))
    result = sp.zeros(3 ** n)
    for ia, a in enumerate(words):
        for ib, b in enumerate(words):
            value = Fraction(0)
            for mask in range(1 << n):
                indices = [i for i in range(n) if mask & (1 << i)]
                if any(a[i] != b[i] for i in range(n)
                       if not mask & (1 << i)):
                    continue
                alpha = [sum(a[i] == j for i in indices) for j in range(3)]
                beta = [sum(b[i] == j for i in indices) for j in range(3)]
                if alpha != beta:
                    continue
                alpha[0] += 1
                value += (-1) ** len(indices) * haar_moment(alpha)
            value /= 2 ** n
            result[ia, ib] = sp.Rational(value.numerator, value.denominator)
    return result


def swap_matrix(n, first, second):
    words = list(product(range(3), repeat=n))
    lookup = {word: i for i, word in enumerate(words)}
    result = sp.zeros(3 ** n)
    for column, word in enumerate(words):
        other = list(word)
        other[first], other[second] = other[second], other[first]
        result[lookup[tuple(other)], column] = 1
    return result


def central_transpositions(n):
    return sum((swap_matrix(n, i, j)
                for i in range(n) for j in range(i + 1, n)),
               sp.zeros(3 ** n))


def partial_transpose_first(matrix, n):
    words = list(product(range(3), repeat=n))
    lookup = {word: i for i, word in enumerate(words)}
    result = sp.zeros(3 ** n)
    for ia, a in enumerate(words):
        for ib, b in enumerate(words):
            row = (b[0],) + a[1:]
            column = (a[0],) + b[1:]
            result[lookup[row], lookup[column]] = matrix[ia, ib]
    return result


def n3_projectors(B):
    """Joint spectral projectors of B and the S3 central transposition sum."""
    I = sp.eye(27)
    C = central_transpositions(3)
    specifications = [
        (-3, [(sp.Rational(0), 1, 1)]),
        (0, [(sp.Rational(1, 160), 4, 2),
             (sp.Rational(1, 120), 6, 1),
             (sp.Rational(1, 80), 2, 1),
             (sp.Rational(1, 60), 4, 0)]),
        (3, [(sp.Rational(1, 120), 1, 3),
             (sp.Rational(1, 80), 2, 2),
             (sp.Rational(1, 60), 3, 1),
             (sp.Rational(1, 48), 4, 0)]),
    ]
    zero_count = sp.diag(*[word.count(0)
                          for word in product(range(3), repeat=3)])
    sx = sp.Matrix([[0, 0, 0], [0, 0, 1], [0, 1, 0]]) / 2
    sy = sp.Matrix([[0, 0, 0], [0, 0, -sp.I], [0, sp.I, 0]]) / 2
    sz = sp.diag(0, sp.Rational(1, 2), sp.Rational(-1, 2))
    collective = []
    for generator in (sx, sy, sz):
        total = sp.zeros(27)
        for site in range(3):
            factors = [generator if i == site else sp.eye(3) for i in range(3)]
            total += sp.kronecker_product(*factors)
        collective.append(total)
    casimir = sum((generator * generator for generator in collective),
                  sp.zeros(27))
    projectors = []
    for central, entries in specifications:
        Pc = I
        for other in (-3, 0, 3):
            if other != central:
                Pc = Pc * (C - other * I) / (central - other)
        for eigenvalue, rank, count in entries:
            R = Pc
            for other, _, _ in entries:
                if other != eigenvalue:
                    R = R * (B - other * I) / (eigenvalue - other)
            require(R == R.T, "Projector is not Hermitian")
            require(R * R == R, "Spectral polynomial is not a projector")
            require(B * R == eigenvalue * R, "Wrong B eigenvalue")
            require(C * R == central * R, "Wrong central eigenvalue")
            require(sp.trace(R) == rank, "Wrong projector rank")
            require(zero_count * R == count * R, "Wrong dark-index count")
            multiplicity = 2 if central == 0 else 1
            spin = (sp.Rational(rank, multiplicity) - 1) / 2
            require(casimir * R == spin * (spin + 1) * R,
                    "Wrong bright SU(2) spin")
            for generator in collective:
                require(generator * R == R * generator,
                        "Projector does not commute with the stabilizer")
            require(zero_count * R == count * R, "Wrong U(1) charge")
            projectors.append((central, eigenvalue, rank, R))
    require(sum((entry[3] for entry in projectors), sp.zeros(27)) == I,
            "Projectors do not sum to identity")
    for i, first in enumerate(projectors):
        for second in projectors[i + 1:]:
            require(first[3] * second[3] == sp.zeros(27),
                    "Projectors are not orthogonal")
    for first, second in ((0, 1), (1, 2)):
        S = swap_matrix(3, first, second)
        require(S * B == B * S, "B is not permutation invariant")
        for _, _, _, R in projectors:
            require(S * R == R * S, "R is not permutation invariant")
    return projectors


def polynomial_ray_integral(expression, variables):
    """Integrate a polynomial in (f0,f1,f2,bar f0,bar f1,bar f2)."""
    result = 0
    for powers, coefficient in sp.Poly(sp.expand(expression), *variables).terms():
        alpha, beta = powers[:3], powers[3:]
        if alpha == beta:
            moment = haar_moment(alpha)
            result += coefficient * sp.Rational(moment.numerator, moment.denominator)
    return sp.expand(result)


def check_posterior_formulas():
    z = sp.symbols("z0:3")
    bar = sp.symbols("b0:3")
    r, s = sp.symbols("r s", real=True)
    A = sp.diag(1, 0, 0)
    B = sp.Matrix([r, s, 0]) * sp.Matrix([[r, s, 0]])
    u = z[0] * bar[0]
    v = (r * z[0] + s * z[1]) * (r * bar[0] + s * bar[1])
    probabilities = [sp.Rational(9, 4) * (1 - u) ** 2 * (1 - v),
                     sp.Rational(9, 8) * u * (1 - v)]
    claimed = [((52 + 8 * r ** 2) * sp.eye(3)
                - (28 + 4 * r ** 2) * A - 20 * B
                + 8 * (A * B + B * A)) / 160,
               sp.Rational(3, 160) * ((4 - r ** 2) * sp.eye(3)
                                     + 4 * A - B - A * B - B * A)]
    for probability, expected in zip(probabilities, claimed):
        actual = sp.Matrix(3, 3,
                           lambda i, j: polynomial_ray_integral(
                               z[i] * bar[j] * probability, z + bar))
        for difference in actual - expected:
            reduced = sp.rem(sp.Poly(difference, s),
                             sp.Poly(s ** 2 + r ** 2 - 1, s)).as_expr()
            require(sp.expand(reduced) == 0, "Wrong posterior moment formula")

    c = sp.symbols("c", real=True)
    fidelity_s = (13 + 2 * c) / 40
    fidelity_a = 3 * (11 - 4 * c + sp.sqrt(25 - 24 * c)) / 320
    # The 2x2 block of 4A-B-AB-BA has this trace and discriminant.
    T = 4 * A - B - A * B - B * A
    trace = T[0, 0] + T[1, 1]
    discriminant = (T[0, 0] - T[1, 1]) ** 2 + 4 * T[0, 1] * T[1, 0]
    for actual, expected in ((trace, 3 - 2 * r ** 2),
                             (discriminant, 25 - 24 * r ** 2)):
        reduced = sp.rem(sp.Poly(actual - expected, s),
                         sp.Poly(s ** 2 + r ** 2 - 1, s)).as_expr()
        require(sp.expand(reduced) == 0, "Wrong antisymmetric eigenvalue")
    integral_s = sp.integrate(2 * (1 - c) * fidelity_s, (c, 0, 1))
    integral_a = sp.integrate(2 * (1 - c) * fidelity_a, (c, 0, 1))
    require(integral_s == sp.Rational(41, 120), "Wrong symmetric integral")
    require(integral_a == sp.Rational(463, 3600), "Wrong antisymmetric integral")
    total = integral_s + integral_a
    require(total == sp.Rational(1693, 3600), "Wrong covariant fidelity")
    finite = sum(weight * (fidelity_s + fidelity_a).subs(c, overlap)
                 for overlap, weight in [(1, sp.Rational(1, 12)),
                                         (0, sp.Rational(1, 6)),
                                         (sp.Rational(1, 3), sp.Rational(3, 4))])
    expected_finite = sp.Rational(41, 120) + (127 + 9 * sp.sqrt(17)) / 1280
    require(sp.simplify(finite - expected_finite) == 0,
            "Wrong finite-MUB fidelity")
    return total, finite


def check_n2():
    B = moment_operator(2)
    I, S = sp.eye(9), swap_matrix(2, 0, 1)
    Pplus, Pminus = (I + S) / 2, (I - S) / 2
    require(B * S == S * B, "N=2 parity invariance failed")
    upper_operator = Pplus / 20 + Pminus / 24
    slack = upper_operator - B
    require(all(value >= 0 for value in slack.eigenvals()),
            "N=2 collective dual is not positive")
    fidelity = sp.trace(upper_operator)
    require(fidelity == sp.Rational(17, 40), "Wrong N=2 objective")
    # Completeness of each rank-one one-copy POVM gives sum w=3,sum wc=1.
    achieved = sp.Rational(1, 4) * 3 * (11 * 3 + 1) / 60
    require(achieved == fidelity, "N=2 one-copy achievement does not match")
    return 1 - fidelity


def check_n3_certificate():
    path = Path(__file__).with_name("ppt_n3_certificate.json")
    certificate = json.loads(path.read_text())
    B = moment_operator(3)
    require(B == B.T, "B is not Hermitian")
    projectors = n3_projectors(B)
    Y = sp.Matrix(certificate["Y_numerator"]) / sp.Integer(certificate["Y_denominator"])
    require(Y.shape == (27, 27) and Y == Y.T,
            "Certificate matrix has wrong shape or symmetry")
    L, diagonal = Y.LDLdecomposition(hermitian=False)
    require(L * diagonal * L.T == Y, "Exact LDL reconstruction failed")
    require(all(pivot > 0 for pivot in diagonal.diagonal()),
            "Certificate matrix is not positive definite")
    lam = dict(zip((-3, 0, 3), map(sp.Rational, certificate["lambda"])))
    slacks = []
    for central, _, rank, R in projectors:
        slack = (lam[central] * rank - sp.trace(B * R)
                 - sp.trace(Y * partial_transpose_first(R, 3)))
        require(slack >= 0, "A rational dual inequality failed")
        slacks.append(slack)
    objective = lam[-3] + 16 * lam[0] + 10 * lam[3]
    require(objective == sp.Rational(certificate["objective"]),
            "Saved objective does not match the dual")
    require(objective == sp.Rational(46264989, 100000000),
            "Unexpected certified objective")
    if "slacks" in certificate:
        require(slacks == list(map(sp.Rational, certificate["slacks"])),
                "Saved slacks do not match recomputation")
    return objective, min(diagonal.diagonal()), min(slacks)


def main():
    n2_risk = check_n2()
    continuous, finite = check_posterior_formulas()
    one_copy_upper, pivot, slack = check_n3_certificate()
    require(continuous > one_copy_upper, "Continuous separation failed")
    # Avoid relying on a floating comparison involving sqrt(17).
    require(finite.subs(sp.sqrt(17), 4) > one_copy_upper,
            "Finite-MUB separation failed")
    print("PASS: exact N=2 minimax risk =", n2_risk)
    print("PASS: covariant pair-plus-single fidelity =", continuous)
    print("PASS: finite-MUB fidelity =", finite)
    print("PASS: all-adaptive-one-copy fidelity <=", one_copy_upper)
    print("PASS: exact dual min LDL pivot =", pivot)
    print("PASS: exact dual min scalar slack =", slack)
    print("PASS: continuous fidelity gap =", continuous - one_copy_upper)
    print("PASS: finite-MUB fidelity gap >",
          finite.subs(sp.sqrt(17), 4) - one_copy_upper)


if __name__ == "__main__":
    main()
