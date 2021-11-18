from itertools import combinations
from hypothesis import given, example
from hypothesis.strategies import integers


class CombinationIterator:

    def __init__(self, characters: str, combinationLength: int):
        self.n = len(characters)
        self.k = combinationLength
        self.c = list(range(self.k))
        self.characters = characters
        self.done = False

    def next(self) -> str:
        result = ''.join(self.characters[i] for i in self.c)

        for j in range(self.k-1, -1, -1):
            if self.c[j] < self.n-self.k+j:
                self.c[j:] = range(self.c[j]+1, self.c[j]+1+self.k-j)
                break
        else:
            self.done = True

        return result

    def hasNext(self) -> bool:
        return not self.done


class CombinationIteratorFun0:

    def __init__(self, characters: str, combinationLength: int):
        self.n = len(characters)
        self.k = combinationLength
        self.c = list(range(self.k))
        self.characters = characters
        self.done = False
        #print("----", characters, combinationLength)

    def next(self) -> str:
        result = ''.join(self.characters[i] for i in self.c)

        j = self.k - 1
        while j >= 0 and self.c[j] == self.n - self.k + j:
            j -= 1

        if j == -1:
            self.done = True
        else:
            self.c[j] += 1
            for i in range(j+1, self.k):
                self.c[i] = self.c[i-1] + 1

        return result

    def hasNext(self) -> bool:
        return not self.done


class CombinationIteratorReingold:

    def __init__(self, characters: str, combinationLength: int):
        self.n = len(characters)
        self.k = combinationLength
        self.c = [-1] + list(range(1, self.k+1))
        self.characters = characters
        self.done = False
        #print("----", characters, combinationLength)

    def next(self) -> str:
        result = ''.join(self.characters[i-1] for i in self.c[1:])

        j = self.k
        while self.c[j] == self.n - self.k + j:
            j -= 1

        self.c[j] += 1
        for i in range(j+1, self.k+1):
            self.c[i] = self.c[i-1] + 1

        if j == 0:
            self.done = True

        return result

    def hasNext(self) -> bool:
        return not self.done


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
    s = "abcdefghijk"[:u+v]
    print(f'-- {s} {v}')
    ci = CombinationIterator(s, v)
    for comb in combinations(s, v):
        assert ci.hasNext()
        comb0 = ci.next()
        #print(comb0, ''.join(comb))
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
