import math, pytest
from itertools import chain
class SolutionTroll:
    def nthMagicalNumber(self, n: int, a: int, b: int) -> int:
        l = math.lcm(a, b)
        s = list(sorted(set(chain(range(0, l, a), range(0, l, b)))))
        q, r = divmod(n, len(s))
        return (q*l + s[r])%(10**9 + 7)

def gen_s(a, b):
    l = math.lcm(a, b)
    s = list(sorted(set(chain(range(0, l, a), range(0, l, b)))))
    return s

class STroll:
    def __init__(self, a, b):
        self.l = math.lcm(a, b)
        self.s = list(sorted(set(chain(range(0, self.l, a), range(0, self.l, b)))))

    def __len__(self):
        return len(self.s)

    def __getitem__(self, i):
        if not (0 <= i < len(self.s)):
            raise IndexError
        return self.s[i]

class S:
    def __init__(self, a, b):
        self.a, self.b = a, b
        self.l = math.lcm(a, b)
        self.ls = self.l // a + self.l // b - 1
        self.s = list(sorted(set(chain(range(0, self.l, a), range(0, self.l, b)))))
        ok = True
        for idx, i in enumerate(self.s):
            cand = (i) // (self.a) + (i) // (self.b)
            print(idx, i, cand, self.s[cand])
            if cand != idx:
                ok = False
        assert ok


    def __len__(self):
        assert len(self.s) == self.ls
        return self.ls

    def A__getitem__(self, i):
        print(f'getitem[{i}]')
        if not (0 <= i < self.ls):
            print(i, self.ls)
            raise IndexError

        lb, ub = 0, self.ls
        while lb < ub:
            #assert 0 <= lb < ub <= self.ls
            #assert lb <= self.s[i] < ub, (lb, self.s[i], ub)
            mid = (lb + ub) // 2
            print( f'lb, mid, ub: {lb} {mid} {ub}')
            
            cand = mid // self.a + mid // self.b
            if cand == i and (mid % self.a == 0 or mid % self.b == 0):
                return mid
            elif cand == i:
                ub = mid
            elif cand < i:
                lb = mid + 1
            else:
                ub = mid
        print( f'lb, ub: {lb} {ub}')

        assert self.s[i] == lb

        return lb

    def __getitem__(self, i):
        print(f'getitem[{i}]')
        if not (0 <= i < self.ls):
            print(i, self.ls)
            raise IndexError

        rr = (i*self.a*self.b + self.a + self.b - 1)//(self.a+self.b)

        r = min( self.a*((rr + self.a - 1)//self.a), 
                 self.b*((rr + self.b - 1)//self.b))

        assert self.s[i] == r

        return r
    
#@pytest.mark.skip
def test_S0():
    s = S(2, 1)
    assert(len(s) == 2)
    print(list(s))
    assert s[0] == 0
    assert s[1] == 1

#@pytest.mark.skip
def test_S1():
    s = S(2, 3)
    assert(len(s) == 4)
    print(list(s))
    assert s[0] == 0
    assert s[1] == 2
    assert s[2] == 3
    assert s[3] == 4


class Solution:
    def nthMagicalNumber(self, n: int, a: int, b: int) -> int:
        l = math.lcm(a, b)
        s = S(a, b)
        q, r = divmod(n, len(s))
        return (q*l + s[r])%(10**9 + 7)

class SolutionAcceptable:
    def nthMagicalNumber(self, n: int, a: int, b: int) -> int:
        l = math.lcm(a, b)
        ls = l // a + l // b - 1
        MOD = 10**9 + 7
        start = 1
        end = min(a,b)*n


        while end - start > 1: 
            m = (end + start)//2
            if m//a +  m//b -  m//l >= n: 
                end = m
            else: 
                start = m
                
        return (end) % MOD

class SolutionInfiniteLoop:
    def nthMagicalNumber(self, n: int, a: int, b: int) -> int:
        M = 10**9 + 7
        bigger, smaller = max(a, b), min(a, b)
        LCM = math.lcm(a, b)
        smallerMagicalNumbers, biggerMagicalNumbers = LCM//a, LCM//b
        totalMagicalNumbers = smallerMagicalNumbers + biggerMagicalNumbers

        index = (n-1) % + 1
        extra = (n-1) // totalMagicalNumbers

        if index == totalMagicalNumbers:
            return (LCM * (extra + 1)) % M
        else:
            left = smaller
            right = LCM
            while True:
                print(left, right)
                mid = left + (right-left)//2
                if mid//a + mid//b == index:
                    if left == right:
                        break
                    else:
                        right = mid
                elif mid//a + mid//b < index:
                    left = mid+1
                else:
                    right = mid-1
            return (extra*LCM+left)%M


#@pytest.mark.skip
def test_A():
    assert Solution().nthMagicalNumber(n=1, a=2, b=3) == 2
    assert Solution().nthMagicalNumber(n=4, a=2, b=3) == 6
    assert Solution().nthMagicalNumber(n=5, a=2, b=4) == 10
    assert Solution().nthMagicalNumber(n=3, a=6, b=4) == 8
