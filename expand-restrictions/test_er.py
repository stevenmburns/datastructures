
import math
from dataclasses import dataclass
from typing import List
from itertools import product
from functools import reduce


@dataclass
class OredTerm:
    offsets: List[int]
    scalings: List[int]


@dataclass
class Restriction:
    period: int
    ored_terms: List[OredTerm]

    def check(self, x, scaling):
        return any((x % self.period) in ored_term.offsets and
                   scaling in ored_term.scalings
                   for ored_term in self.ored_terms)


def simplify(pairs):
    offsets_with_pos_scaling = {o for o, s in pairs if s == 1}
    offsets_with_neg_scaling = {o for o, s in pairs if s == -1}
    offsets_with_both_scalings = offsets_with_pos_scaling.intersection(offsets_with_neg_scaling)
    offsets_with_pos_scaling -= offsets_with_both_scalings
    offsets_with_neg_scaling -= offsets_with_both_scalings
    if offsets_with_both_scalings:
        yield OredTerm(sorted(offsets_with_both_scalings), [1, -1])
    if offsets_with_pos_scaling:
        yield OredTerm(sorted(offsets_with_pos_scaling), [1])
    if offsets_with_neg_scaling:
        yield OredTerm(sorted(offsets_with_neg_scaling), [-1])


def lcm(*xs):
    def lcm2(a, b):
        return (a*b) // math.gcd(a, b)
    return reduce(lcm2, xs)


def test_lcm():
    assert lcm(2, 3) == 6
    assert lcm(2, 3, 4) == 12
    assert lcm(2, 3, 4, 5) == 60
    assert lcm(2, 3, 4, 5, 6) == 60


def merge(*rs):
    new_period = lcm(*(r.period for r in rs))

    def gen_pairs(r):
        for coarse_offset in range(0, new_period, r.period):
            for ored_term in r.ored_terms:
                for offset, scaling in product(ored_term.offsets, ored_term.scalings):
                    yield (coarse_offset + offset, scaling)

    pairs = set.intersection(*(set(gen_pairs(r)) for r in rs))
    return Restriction(new_period, list(simplify(pairs)))


def test_A0():
    r0 = Restriction(2, [OredTerm([0], [1])])
    r1 = Restriction(3, [OredTerm([0], [1])])

    assert r0.check(0, 1)
    assert not r0.check(1,  1)
    assert r0.check(2, 1)
    assert r1.check(0, 1)
    assert not r1.check(1,  1)
    assert r1.check(3, 1)
    assert not r1.check(0, -1)


def test_A1():
    r0 = Restriction(4, [OredTerm([0, 1, 3], [1])])
    r1 = Restriction(6, [OredTerm([0, 1, 2], [1, -1])])
    r = merge(r0, r1)
    print(r)


def test_A2():
    r0 = Restriction(4, [OredTerm([0], [-1]), OredTerm([1], [1])])
    r1 = Restriction(6, [OredTerm([0, 1, 2], [1, -1])])
    r = merge(r0, r1)
    print(r)


def test_A3():
    r0 = Restriction(4, [OredTerm([0, 1], [1])])
    r1 = Restriction(6, [OredTerm([0, 1, 2], [1])])
    r = merge(r0, r1)
    print(r)


def test_A4():
    r0 = Restriction(2, [OredTerm([0], [1])])
    r1 = Restriction(3, [OredTerm([0, 1], [1])])
    r = merge(r0, r1)
    print(r)
