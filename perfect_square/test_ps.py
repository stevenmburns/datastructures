class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        lo = 1
        hi = num+1

        while True:
            mid = (lo+hi-1)//2
            #print(f'lo: {lo} mid: {mid} hi: {hi}, {lo*lo} <= {num} < {hi*hi}')
            #assert lo*lo <= num < hi*hi
            #assert lo <= mid < hi
            
            cand0 = mid*mid
            cand1 = (mid+1)*(mid+1)
            
            if cand1 < num:
                lo = mid+1
            elif num < cand0:
                hi = mid
            elif cand0 == num or cand1 == num:
                return True
            else:
                return False
            


def test_A0():
    assert Solution().isPerfectSquare(1) == True
    assert Solution().isPerfectSquare(16) == True
    assert Solution().isPerfectSquare(14) == False
    assert Solution().isPerfectSquare(4) == True
    assert Solution().isPerfectSquare(2147483647) == False
    assert Solution().isPerfectSquare(2147483648) == False