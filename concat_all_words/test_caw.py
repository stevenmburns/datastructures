from typing import List
from collections import defaultdict, Counter

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        m = len(words)
        n = len(words[0])
        word_bag = Counter(words)
        res = []
        for i in range(len(s)):
            found = defaultdict(int)
            for j in range(0, m*n, n):
                lb = i+j
                ub = lb+n
                if ub > len(s):
                    break
                cand = s[lb:ub]
                if cand in word_bag and (found[cand] < word_bag[cand]):
                    found[cand] += 1
                else:
                    break
            else:
                if set(found.keys()) == set(word_bag.keys()):
                    if (all(found[w] == word_bag[w] for w in word_bag)):
                        res.append(i)
                
        return res

def test_A0():
    s = "barfoothefoobarman"
    words = ["foo","bar"]
    assert set(Solution().findSubstring(s, words)) == {0, 9}

def test_A1():
    s = "wordgoodgoodgoodbestword"
    words = ["word","good","best","good"]
    assert set(Solution().findSubstring(s, words)) == {8}