from itertools import combinations
from hypothesis import given, example
from hypothesis.strategies import integers


class CombinationIteratorReingold:

    def __init__(self, characters: str, combinationLength: int):
        self.n = len(characters)
        self.t = combinationLength
        self.c = [-1] + list(range(1, self.t+1))
        self.characters = characters
        self.done = False
        self.j = 1
        print("----", characters, combinationLength)

    def next(self) -> str:
        result = ''.join(self.characters[i-1] for i in self.c[1:])

        self.j = self.t
        while self.c[self.j] == self.n - self.t + self.j:
            self.j -= 1

        self.c[self.j] += 1
        for i in range(self.j+1, self.t+1):
            self.c[i] = self.c[i-1] + 1

        return result

    def hasNext(self) -> bool:
        return self.j != 0


CombinationIterator = CombinationIteratorReingold


class CombinationIteratorKnuth:

    def __init__(self, characters: str, combinationLength: int):
        self.n = len(characters)
        self.t = combinationLength
        self.a = list(range(self.t))
        self.a.extend([self.n, 0])
        self.characters = ''.join(characters)
        self.done = False
        print("----", characters, combinationLength)

    def geta(self, i: int) -> int:
        return self.a[i]

    def next(self) -> str:
        result = ''.join(self.characters[i] for i in self.a[:self.t])

        j = 0
        while self.a[j] + 1 == self.a[j+1]:
            self.a[j] = j
            j += 1

        self.done = j >= self.t
        self.a[j] += 1

        print(self.a, result)

        return result

    def hasNext(self) -> bool:
        return not self.done


# Your CombinationIterator object will be instantiated and called as such:
# obj = CombinationIterator(characters, combinationLength)
# param_1 = obj.next()
# param_2 = obj.hasNext()


def test_A0():
    ci = CombinationIterator("abc", 2)
    assert ci.hasNext()
    assert ci.next() == "ab"
    assert ci.hasNext()
    assert ci.next() == "ac"
    assert ci.hasNext()
    assert ci.next() == "bc"
    assert not ci.hasNext()


@ given(integers(min_value=1, max_value=5), integers(min_value=1, max_value=5))
@ example(2, 2)
def test_A2(u, v):
    ci = CombinationIterator("abcdefghijk"[:u+v], v)
    for comb in combinations("abcdefghijk"[:u+v], v):
        assert ci.hasNext()
        comb0 = ci.next()
        print(comb0, ''.join(comb))
        assert comb0 == ''.join(comb)

    assert not ci.hasNext()


def test_A1():
    ci = CombinationIterator("abcd", 2)
    assert ci.hasNext()
    assert ci.next() == "ab"
    assert ci.hasNext()
    assert ci.next() == "ac"
    assert ci.hasNext()
    assert ci.next() == "ad"
    assert ci.hasNext()
    assert ci.next() == "bc"
    assert ci.hasNext()
    assert ci.next() == "bd"
    assert ci.hasNext()
    assert ci.next() == "cd"
    assert not ci.hasNext()
