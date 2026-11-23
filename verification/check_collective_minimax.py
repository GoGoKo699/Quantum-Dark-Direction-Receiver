#!/usr/bin/env python3
"""Verify the finite collective and three-qutrit formulas in exact arithmetic.

The finite tests use only Python and SymPy. The checks enumerate small
specimen budgets. The scientific proofs establish the unrestricted quantifiers.
"""
from collections import Counter, defaultdict
from itertools import combinations, product
from math import factorial, prod

import sympy as sp

from check_finite_budget import (
    central_transpositions,
    moment_operator,
    n3_projectors,
    require,
    swap_matrix,
)


def partitions(total, rows, largest=None):
    """Partitions padded with zero rows."""
    if rows == 0:
        if total == 0:
            yield ()
        return
    if largest is None:
        largest = total
    for first in range(min(total, largest), -1, -1):
        for remainder in partitions(total - first, rows - 1, first):
            yield (first,) + remainder


def weyl_dimension(shape):
    return prod(sp.Rational(shape[i] - shape[j] + j - i, j - i)
                for i, j in combinations(range(len(shape)), 2))


def specht_dimension(shape):
    hooks = (row - j + sum(lower > j for lower in shape[i + 1:])
             for i, row in enumerate(shape) for j in range(row))
    return factorial(sum(shape)) // prod(hooks)


def content_sum(shape):
    return sum(j - i for i, row in enumerate(shape) for j in range(row))


def conditional_fidelity(shape):
    d = len(shape)
    return prod(sp.Rational(row + d - i - 1, row + d - i)
                for i, row in enumerate(shape[:-1]))


def moment_block(words, dimension):
    """Haar score and sum of transpositions on a fixed occupation block."""
    n = len(words[0])
    moments = [factorial(a) for a in range(n + 2)]
    swap_sum = sp.zeros(len(words))
    score = sp.zeros(len(words))
    indices = {word: j for j, word in enumerate(words)}
    for col, word in enumerate(words):
        for u, v in combinations(range(n), 2):
            swapped = list(word)
            swapped[u], swapped[v] = word[v], word[u]
            swap_sum[indices[tuple(swapped)], col] += 1
    for row, a in enumerate(words):
        for col in range(row, len(words)):
            b = words[col]
            changed = tuple(i for i in range(n) if a[i] != b[i])
            unchanged = tuple(i for i in range(n) if a[i] == b[i])
            entry = sp.S.Zero
            for count in range(len(unchanged) + 1):
                for extra in combinations(unchanged, count):
                    active = changed + extra
                    powers = Counter(a[i] for i in active)
                    if powers != Counter(b[i] for i in active):
                        continue
                    powers[0] += 1
                    numerator = (-1) ** len(active) * factorial(dimension - 1)
                    numerator *= prod(moments[p] for p in powers.values())
                    entry += sp.Rational(numerator,
                                         factorial(len(active) + dimension))
            score[row, col] = score[col, row] = entry / (dimension - 1) ** n
    return score, swap_sum


def check_collective(dimension, specimen_count):
    shapes = list(partitions(specimen_count, dimension))
    by_content = {content_sum(shape): shape for shape in shapes}
    require(len(by_content) == len(shapes), "Probe has colliding contents")
    expected_ranks = {}
    expected_peaks = {}
    expected_bright_ranks = {}
    formula = 0
    weight_sum = 0
    for shape in shapes:
        whole = weyl_dimension(shape)
        multiplicity = specht_dimension(shape)
        rank = 0 if shape[-1] else weyl_dimension(shape[:-1])
        denominator = sp.Integer(dimension - 1) ** specimen_count
        weight = rank * multiplicity / denominator
        weight_sum += weight
        conditional = conditional_fidelity(shape)
        formula += weight * conditional
        expected_ranks[shape] = whole * multiplicity
        expected_bright_ranks[shape] = rank * multiplicity
        expected_peaks[shape] = rank * conditional / (whole * denominator)
    require(weight_sum == 1, "Schur weights do not normalize")

    occupations = defaultdict(list)
    for word in product(range(dimension), repeat=specimen_count):
        occupations[tuple(word.count(i) for i in range(dimension))].append(word)
    ranks = defaultdict(int)
    bright_ranks = defaultdict(int)
    fidelity = 0
    for occupation, words in occupations.items():
        score, swap_sum = moment_block(words, dimension)
        require(score * swap_sum == swap_sum * score,
                "Score does not preserve the central eigenspaces")
        for contents, multiplicity, vectors in swap_sum.eigenvects():
            shape = by_content[contents]
            peak = expected_peaks[shape]
            ranks[shape] += multiplicity
            basis = sp.Matrix.hstack(*vectors)
            # A pivot set identifies coordinates of a vector in this eigenspace.
            pivots = list(basis.T.rref()[1])
            restricted = basis[pivots, :].inv() * (score * basis)[pivots, :]
            fidelity += peak * multiplicity
            if shape[-1]:
                require(restricted.is_zero_matrix, "Unsupported sector scores")
            elif occupation[0] == 0:
                require(restricted == peak * sp.eye(multiplicity),
                        "Bright block does not attain the formula")
                bright_ranks[shape] += multiplicity
            else:
                require(all(value.is_Rational and value < peak
                            for value in restricted.eigenvals()),
                        "A block with dark occupation reaches the bright peak")
    require(dict(ranks) == expected_ranks, "Wrong Schur sector ranks")
    require(all(bright_ranks[shape] == rank
                for shape, rank in expected_bright_ranks.items()),
            "Wrong bright top eigenspace ranks")
    require(fidelity == formula, "Incorrect finite collective fidelity")
    return 1 - fidelity


def check_qutrit_score_blocks():
    """Reconstruct the qutrit deficit on a product with an antisymmetric pair."""
    score = moment_operator(3)
    identity = sp.eye(27)
    swaps = central_transpositions(3)
    symmetric = swaps * (swaps + 3 * identity) / 18
    determinant = swaps * (swaps - 3 * identity) / 18
    mixed = identity - symmetric - determinant
    upper = symmetric / 48 + mixed / 60
    deficit = upper - score
    projectors = n3_projectors(score)
    require(all(sp.trace(deficit * projector) >= 0
                for _, _, _, projector in projectors),
            "The score upper bound is not positive")

    e0, e1, e2 = [sp.eye(3)[:, i] for i in range(3)]
    tensor = sp.kronecker_product
    wedge12 = (tensor(e1, e2) - tensor(e2, e1)) / sp.sqrt(2)
    wedge02 = (tensor(e0, e2) - tensor(e2, e0)) / sp.sqrt(2)
    wedge01 = (tensor(e0, e1) - tensor(e1, e0)) / sp.sqrt(2)
    dark, bright = sp.symbols("dark bright", real=True)
    one = dark * e0 + bright * e1
    embed = sp.Matrix.hstack(
        *[tensor(one, wedge) for wedge in (wedge12, wedge02, wedge01)])
    component = sp.Matrix([dark, -bright, 0])
    determinant_form = component * component.T / 3
    require(sp.expand(embed.T * determinant * embed) == determinant_form,
            "Wrong alternating weight for a product across the cut")
    expected = sp.diag(dark ** 2, sp.Rational(3, 2) + dark ** 2,
                       2 + dark ** 2 / 2) - determinant_form
    difference = 240 * embed.T * deficit * embed - expected
    relation = sp.Poly(bright ** 2 + dark ** 2 - 1, bright)
    require(all(sp.rem(sp.Poly(entry, bright), relation).is_zero
                for entry in difference),
            "Wrong restricted score deficit")

    pair_antisymmetric = (identity - swap_matrix(3, 1, 2)) / 2
    require(sp.trace(pair_antisymmetric) == 9
            and sp.trace(mixed + determinant) == 17,
            "Wrong trace budgets for the converse")
    require(symmetric * pair_antisymmetric == sp.zeros(27)
            and determinant * pair_antisymmetric == determinant,
            "Incorrect support of the antisymmetric pair")
    require(sp.trace(upper * (identity - pair_antisymmetric))
            == sp.Rational(41, 120), "Wrong symmetric-branch fidelity")
    triple_bright = tensor(e1, e1, e1)
    require(deficit * triple_bright == sp.zeros(27, 1)
            and symmetric * triple_bright == triple_bright,
            "The symmetric attaining seed has nonzero deficit")
    return sp.trace(upper)


def check_qutrit_optimized_duals():
    """Check the scalar maximization and its attaining trace allocation."""
    u, t = sp.symbols("u t", positive=True)
    multiplier = sp.Rational(5, 2) / (u ** 2 - 1)
    vertex = (3 * u / 2 - 1) / (u ** 2 - 1)
    cauchy_sum = t / (t + multiplier) + (
        (1 - t) / (sp.Rational(3, 2) + t + multiplier))
    coefficient = sp.cancel(3 / cauchy_sum.subs(t, vertex))
    require(coefficient == (9 * u + 9) / (5 * u - 5),
            "Wrong optimized Cauchy constant")
    require(sp.cancel(sp.diff(cauchy_sum, t).subs(t, vertex)) == 0,
            "Claimed optimizer is not stationary")
    # The derivative changes sign when the strictly decreasing ratio
    # (t+multiplier+3/2)/(t+multiplier) crosses u.
    ratio = (t + multiplier + sp.Rational(3, 2)) / (t + multiplier)
    require(sp.cancel(sp.diff(ratio, t) * (t + multiplier) ** 2)
            == -sp.Rational(3, 2), "Wrong monotonicity in scalar maximization")
    norm = (t / (t + multiplier) ** 2
            + (1 - t) / (sp.Rational(3, 2) + t + multiplier) ** 2)
    det_weight = sp.cancel((cauchy_sum ** 2 / (3 * norm)).subs(t, vertex))
    require(sp.cancel(det_weight - 25 * u / (18 * (u + 1) ** 2)) == 0,
            "Wrong normalized determinant weight")
    scores = {}
    for trace_budget, optimizer, expected in (
        (9, (21 + 5 * sp.sqrt(17)) / 4,
         sp.Rational(83, 192) + 3 * sp.sqrt(17) / 320),
        (17, (389 + 5 * sp.sqrt(6001)) / 36,
         sp.Rational(25, 64) + sp.sqrt(6001) / 960),
    ):
        lower_optimizer = optimizer.subs({sp.sqrt(17): 0, sp.sqrt(6001): 0})
        require(lower_optimizer > 2, "Optimizer does not give a positive multiplier")
        # u>2 puts the displayed stationary t strictly between zero and one.
        require(sp.simplify(trace_budget * det_weight.subs(u, optimizer) - 1)
                == 0, "Seed fails to supply the prescribed determinant trace")
        gap = (coefficient - 1 - trace_budget * multiplier) / 240
        attained = sp.Rational(19, 40) - gap.subs(u, optimizer)
        require(sp.simplify(attained - expected) == 0,
                "The saturated dual has the wrong value")
        scores[trace_budget] = expected
    return scores


def check_qutrit_hierarchy():
    collective = check_qutrit_score_blocks()
    scores = check_qutrit_optimized_duals()
    c = sp.symbols("c", real=True)
    antisymmetric_posterior = 3 * (11 - 4 * c + sp.sqrt(25 - 24 * c)) / 320
    require(sp.simplify(sp.diff(antisymmetric_posterior, c, 2)
                        * (25 - 24 * c) ** sp.Rational(3, 2))
            == -sp.Rational(27, 20), "Posterior score is not strictly concave")
    sequential = sp.Rational(41, 120) + antisymmetric_posterior.subs(
        c, sp.Rational(1, 3))
    require(sequential == scores[9], "Sequential strategy leaves a fixed-cut gap")

    one_copy_upper = sp.Rational(46264989, 100000000)
    # Prove strict comparisons using rational bounds on both radicals.
    require(4 ** 2 < 17 < sp.Rational(33, 8) ** 2, "Bad sqrt(17) bracket")
    lower_sqrt_6001 = sp.Rational(387, 5)
    require(lower_sqrt_6001 ** 2 < 6001 < 78 ** 2, "Bad sqrt(6001) bracket")
    require(one_copy_upper < sequential.subs(sp.sqrt(17), 4),
            "Sequential strategy does not beat the released single-copy bound")
    require(sequential.subs(sp.sqrt(17), sp.Rational(33, 8))
            < scores[17].subs(sp.sqrt(6001), lower_sqrt_6001),
            "Effectwise biseparable strategy does not beat fixed cuts")
    require(scores[17].subs(sp.sqrt(6001), 78) < collective
            == sp.Rational(19, 40), "The collective gap does not hold")
    print("PASS: exact three-qutrit collective fidelity =", collective)
    print("PASS: exact three-qutrit effectwise biseparable fidelity =", scores[17])
    print("PASS: exact three-qutrit fixed-cut and sequential fidelity =", sequential)


def main():
    probes = {
        2: (sp.Rational(1, 3), sp.Rational(1, 4), sp.Rational(1, 5)),
        3: (sp.Rational(5, 8), sp.Rational(23, 40), sp.Rational(21, 40),
            sp.Rational(67, 140), sp.Rational(783, 1792)),
        4: (sp.Rational(11, 15), sp.Rational(193, 270), sp.Rational(656, 945)),
        5: (sp.Rational(19, 24), sp.Rational(263, 336), sp.Rational(2771, 3584)),
    }
    for dimension, risks in probes.items():
        for specimen_count, expected in enumerate(risks, start=1):
            risk = check_collective(dimension, specimen_count)
            require(risk == expected, "A probe gives the wrong exact risk")
            print(f"PASS: d={dimension}, N={specimen_count}, risk={risk}")
    check_qutrit_hierarchy()


if __name__ == "__main__":
    main()
