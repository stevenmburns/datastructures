from typing import List


class Solution:
    def maxCoinsCheat(self, nums):
        nums = [1] + nums + [1]  # add the dummy head and tail, both are left till end and DO NOT burst them.
        dp = [[0] * len(nums) for _ in nums]
        for i in range(len(nums) - 3, -1, -1):
            for j in range(i + 2, len(nums)):
                dp[i][j] = max([dp[i][k] + dp[k][j] + nums[i] * nums[k] * nums[j] for k in range(i + 1, j)])
        return dp[0][len(nums) - 1]

    def maxCoins(self, nums: List[int]) -> int:
        n = len(nums)

        nums = [1] + nums + [1]

        d = [[0] * (n + 2) for _ in range(n + 2)]

        for q in range(n):
            for i in range(n-q):
                j = i + q
                prod0 = nums[(i-1)+1] * nums[(j+1)+1]
                d[i+1][j+1] = max(d[i+1][k] + d[k+2][j+1] + prod0 * nums[k+1] for k in range(i, j+1))

        return d[1][n]


def test_A0():
    assert 167 == Solution().maxCoins([3, 1, 5, 8])


def test_A1():
    assert 10 == Solution().maxCoins([1, 5])


def xtest_A2():
    assert 498010100 == Solution().maxCoins([100] * 500)


def test_A3():
    assert 198010100 == Solution().maxCoins([100] * 200)
