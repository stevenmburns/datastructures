
import math
from dataclasses import dataclass
from typing import List


@dataclass
class OredTerm:
    offsets: List[int]
    scalings: List[int]


@dataclass
class Restriction:
    period: int
    ored_terms: List[OredTerm]

    def check(self, x, scaling):
        x0 = x % self.period

        return any(x0 in ored_term.offsets and scaling in ored_term.scalings for ored_term in self.ored_terms)


def merge(r0, r1):

    new_period = math.lcm(r0.period, r1.period)

    def gen_pairs(r):
        for coarse_offset in range(0, r0.period, new_period):
            for ored_term in r0.ored_terms:
                for offset in ored_term.offsets:
                    for scaling in ored_term.scalings:
                        yield (coarse_offset + offset, scaling)

    ored_terms0 = set(gen_pairs(r0))
    ored_terms1 = set(gen_pairs(r1))

    ored_terms = ored_terms0.intersection(ored_terms1)

    return Restriction(new_period, [OredTerm([o], [s]) for o, s in ored_terms])


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
    r0 = Restriction(2, [OredTerm([0], [1])])
    r1 = Restriction(3, [OredTerm([1], [1])])
    r = merge(r0, r1)
    print(r)
