class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i, j = 0, 0
        cs = set()
        max_len = 0
        while i < len(s) and j < len(s):
            if s[j] not in cs:
                cs.add(s[j])
                j += 1
                max_len = max(max_len, j - i)
            else:
                cs.remove(s[i])
                i += 1

        return max_len


def test_A():
    assert Solution().lengthOfLongestSubstring("abcabcbb") == 3
