from heapq import heappop, heappush


class SolutionAcceptable:
    def nthUglyNumber(self, n: int) -> int:

        q = []
        heappush(q, 1)

        reached = set()

        count = 0

        while True:

            x = heappop(q)

            if x in reached:
                continue

            reached.add(x)
            count += 1

            if count == n:
                return x

            heappush(q, 2*x)
            heappush(q, 3*x)
            heappush(q, 5*x)


class SolutionExceedsExpectations:
    def nthUglyNumber(self, n: int) -> int:
        state = [0, 0, 0]
        dp = [0]*n
        dp[0] = 1

        for i in range(1, n):
            cand = [dp[idx]*f for idx, f in zip(state, [2, 3, 5])]
            dp[i] = min(cand)
            for idx, v in enumerate(cand):
                if v == dp[i]:
                    state[idx] += 1
        return dp[-1]


class Solution:
    def nthUglyNumber(self, n: int) -> int:
        state = [0, 0, 0]
        state2 = [1, 1, 1]
        dp = [0]*n
        dp[0] = 1

        for i in range(1, n):
            print(state, state2, dp)
            assert all(dp[idx]*f == s*f for idx, s, f in zip(state, state2, [2, 3, 5]))
            cand = [dp[idx]*f for idx, f in zip(state, [2, 3, 5])]
            cand2 = [(s*f, f) for s, f in zip(state2, [2, 3, 5])]
            dp[i] = min(cand)
            m, f = min(cand2)
            assert m == dp[i]
            for idx, v in enumerate(cand):
                if v == dp[i]:
                    state[idx] += 1
                    state2[idx] = dp[state[idx]]

        return dp[-1]


def test_A0():
    assert Solution().nthUglyNumber(10) == 12


def test_A1():
    assert Solution().nthUglyNumber(20000) == 15424418419015680000000
