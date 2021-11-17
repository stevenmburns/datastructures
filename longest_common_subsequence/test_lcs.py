
from collections import defaultdict
from hypothesis import given, example
from hypothesis.strategies import lists, sampled_from


class Solution:
    def longestCommonSubsequenceTroll(self, text1: str, text2: str) -> int:
        tbl = {}
        for u in range(len(text1)+1):
            tbl[(u, len(text2))] = 0

        for v in range(len(text2)+1):
            tbl[(len(text1), v)] = 0

        def aux(u, v):
            if (u, v) not in tbl:
                i = text2.find(text1[u], v)
                case0 = 0 if i == -1 else 1 + aux(u+1, i+1)
                case1 = aux(u+1, v)
                tbl[(u, v)] = max(case0, case1)
            return tbl[(u, v)]

        return aux(0, 0)

    def longestCommonSubsequencePoor(self, text1: str, text2: str) -> int:
        tbl = {}
        for u in range(len(text1)+1):
            tbl[(u, 0)] = 0

        for v in range(len(text2)+1):
            tbl[(0, v)] = 0

        def aux(u, v):
            if (u, v) not in tbl:
                assert 0 < u, (u, v)
                i = text2.rfind(text1[u-1], 0, v)
                case0 = 0 if i == -1 else 1 + aux(u-1, i)
                case1 = aux(u-1, v)
                tbl[(u, v)] = max(case0, case1)
            return tbl[(u, v)]

        return aux(len(text1), len(text2))

    def longestCommonSubsequenceExceedsExpectations(self, text1: str, text2: str) -> int:
        row = [0] * (len(text2) + 1)
        for u in range(1, len(text1)+1):
            newrow = [0]
            for v in range(1, len(text2)+1):
                i = text2.rfind(text1[u-1], 0, v)
                case0 = 0 if i == -1 else 1 + row[i]
                case1 = row[v]
                newrow.append(max(case0, case1))
            row = newrow
        return row[-1]

    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        row = [0] * (len(text2) + 1)
        for u in range(1, len(text1)+1):
            newrow = [0]
            chars = {}
            for v in range(1, len(text2)+1):
                c1, c2 = text1[u-1], text2[v-1]
                chars[c2] = v-1
                newrow.append(
                    max(1 + row[chars[c1]] if c1 in chars else 0, row[v]))
            row = newrow
        return row[-1]


def test_A0():
    assert Solution().longestCommonSubsequence("abcde", "ace") == 3
    assert Solution().longestCommonSubsequence("abc", "abc") == 3
    assert Solution().longestCommonSubsequence("abc", "def") == 0
    assert Solution().longestCommonSubsequence("abc", "") == 0
    assert Solution().longestCommonSubsequence("", "abc") == 0
    assert Solution().longestCommonSubsequence("", "") == 0
    assert Solution().longestCommonSubsequence("abc", "defgh") == 0
    assert Solution().longestCommonSubsequence("defgh", "abc") == 0
    assert Solution().longestCommonSubsequence("abc", "abcdef") == 3
    assert Solution().longestCommonSubsequence("abcdef", "abc") == 3
    assert Solution().longestCommonSubsequence("abcdef", "abcdef") == 6
    assert Solution().longestCommonSubsequence("abcdef", "abcdefgh") == 6
    assert Solution().longestCommonSubsequence("abcdefgh", "abcdef") == 6
    assert Solution().longestCommonSubsequence("abcdefgh", "abcdefgh") == 8


def test_A1():
    text1 = "a" * 1000
    text2 = "a" * 999
    assert Solution().longestCommonSubsequence(text1, text2) == 999


@given(lists(sampled_from("abcdefg"), min_size=1, max_size=100),
       lists(sampled_from("abcdefg"), min_size=1, max_size=100))
def test_hypo(l1, l2):
    s1, s2 = ''.join(l1), ''.join(l2)
    assert (v := Solution().longestCommonSubsequence(
        s1, s2)) == Solution().longestCommonSubsequenceTroll(s1, s2)
    print(s1, s2, v)
