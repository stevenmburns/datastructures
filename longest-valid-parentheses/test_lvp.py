
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        dp, st = [0] * (len(s)+1), []
        for idx, c in enumerate(s):
            if c == ')':
                if st:
                    idx0 = st.pop()
                    dp[idx+1] = (idx - idx0 + 1) + dp[idx0]
            else:
                st.append(idx)
        return max(dp)


def test_A0():
    assert Solution().longestValidParentheses("()") == 2


def test_A1():
    assert Solution().longestValidParentheses("(()") == 2


def test_A2():
    assert Solution().longestValidParentheses(")()())") == 4


def test_A3():
    assert Solution().longestValidParentheses("") == 0


def test_A4():
    assert Solution().longestValidParentheses("()(())") == 6
