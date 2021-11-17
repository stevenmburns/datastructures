from typing import DefaultDict, List
from collections import defaultdict, Counter
from random import choice, shuffle
from itertools import combinations
from functools import reduce


class Solution1(object):
    def findNumOfValidWords(self, words, puzzles):
        freq = Counter(frozenset(word) for word in words)

        def gen_subsets(puzzle):
            for i in range(0, len(puzzle)+1):
                for comb in combinations(puzzle, i):
                    yield frozenset(comb)

        return [sum(freq[frozenset(subset | {puzzle[0]})]
                    for subset in gen_subsets(puzzle[1:])) for puzzle in puzzles]


class Solution(object):
    def findNumOfValidWords(self, words, puzzles):
        def bit_mask(word):
            return reduce(lambda x, y: x | (1 << (ord(y) - ord('a'))), word, 0)
        freq = Counter(bit_mask(word) for word in words)

        res = []
        for puzzle in puzzles:
            mask = bit_mask(puzzle[1:])
            first = ord(puzzle[0]) - ord('a')

            def gen_subsets():
                curr = mask
                while curr:
                    yield curr | (1 << first)
                    curr = (curr - 1) & mask
                yield 1 << first

            res.append(sum(freq[subset] for subset in gen_subsets()))
        return res


class Solution2:
    def check(self, word, puzzle):
        return all(c in puzzle for c in word)

    def findNumOfValidWords(self, words: List[str], puzzles: List[str]) -> List[int]:
        chars = "abcdefghijklmnopqrstuvwxyz"
        ctbl = {c: i for i, c in enumerate(chars)}

        def set_to_int(s):
            r = 0
            for c in s:
                r |= 1 << ctbl[c]
            return r

        tbl = defaultdict(list)
        for word in words:
            s = set_to_int(word)
            for c in set(word):
                tbl[c].append(s)
        # for k, v in tbl.items():
            # print('\t', k, len(v), v[:10])
        pp = [(p[0], ~set_to_int(p)) for p in puzzles]
        result = []
        for p0, ps in pp:
            # print(p0, ps)
            s = sum(1 for word in tbl[p0] if not word & ps)
            result.append(s)
        return result


def gen_subsets(mask):
    curr = mask
    while curr:
        yield curr
        curr = (curr - 1) & mask


def test_gen_subsets():
    mask = 0b1101

    def to_set(mask, m):
        return set(i for i in range(m) if mask & (1 << i))

    print(to_set(mask, 4))
    subsets = {frozenset(to_set(subset, 4)) for subset in gen_subsets(mask)}

    subsets2 = set()
    for i in range(1, 4):
        for s in combinations(to_set(mask, 4), i):
            subsets2.add(frozenset(set(s)))

    assert subsets2 == subsets


def test_A0():

    words = ["aaaa", "asas", "able", "ability", "actt", "actor", "access"]
    puzzles = ["aboveyz", "abrodyz", "abslute",
               "absoryz", "actresz", "gaswxyz"]
    output = [1, 1, 3, 2, 4, 0]
    assert Solution().findNumOfValidWords(words, puzzles) == output


def test_A1():
    """puzzles 10000:7, words 100000:4 <= x <= 50"""
    n = 10000
    m = 100000
    chars = "abcdefghijklmnopqrstuvwxyz"
    puzzles = []
    for _ in range(n):
        ss = list(chars)
        shuffle(ss)
        # print(ss)
        puzzles.append(''.join(ss[: 8]))
    words = []
    for _ in range(m):
        l = choice(range(4, 50))
        words.append(''.join(choice(chars) for _ in range(l)))

    print(Solution().findNumOfValidWords(words, puzzles))
