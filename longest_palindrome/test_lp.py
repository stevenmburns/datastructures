from itertools import combinations

def check_palindrome(s):
    l = 0
    u = len(s)
    while l < u:
        if s[l] == s[u-1]:
            l += 1
            u -= 1
        else:
            return False
        
    return True    

class SolutionTroll:
    def longestPalindrome(self, s: str) -> str:
        
        
        def is_palindrome( l, u):
            while l < u:
                if s[l] == s[u-1]:
                    l += 1
                    u -= 1
                else:
                    return False
                
            return True
        
        
        def gen_palidromes():
            for l, u in combinations( range(len(s)+1), 2):
                if is_palindrome(l, u):
                    yield s[l:u]
                    
        return max( gen_palidromes(), key=len)

class SolutionAcceptable:
    def longestPalindrome(self, s: str) -> str:

        if len(s) < 2:
            return s

        longest = ""    
        for center in range(len(s)):
            l = center
            u = center + 1
            while l > 0 and u < len(s):
                if s[l-1] == s[u]:
                    l -= 1
                    u += 1
                else:
                    break
            longest = max(longest, s[l:u], key=len)

            l = center
            u = center
            while l > 0 and u < len(s):
                if s[l-1] == s[u]:
                    l -= 1
                    u += 1
                else:
                    break
            longest = max(longest, s[l:u], key=len)


        return longest


class SolutionExceedsExpectation:
    def longestPalindrome(self, s: str) -> str:
        longest = (0,0) 
        n = len(s)
        
        def centers():
            l = n//2
            u = l+1
            while 0 <= l or u < n:
                if l >= 0:
                    yield l
                    l -= 1
                if u < n:
                    yield u
                    u += 1
                    
                    
        for center in centers():
            if min(center, n-center)*2 + 1 > longest[1]-longest[0]:
                for l, u in [(center, center+1), (center, center)]:
                    while l > 0 and u < n and s[l-1] == s[u]:
                            l, u = l-1, u+1
                    longest = max(longest, (l,u), key=lambda p: p[1]-p[0])
        return s[longest[0]:longest[1]]

class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest = (0,0) 
        n = len(s)
        
        def centers():
            l = n//2
            u = l+1
            while 0 <= l or u < n:
                if l >= 0:
                    yield l
                    l -= 1
                if u < n:
                    yield u
                    u += 1
                    
                    
        for center in centers():
            t = max(0,(longest[1]-longest[0]) // 2 - 1)
            for l, u in [(center-t, center+t+1), (center-t, center+t)]:
                while l > 0 and u < n and s[l-1] == s[u]:
                        l, u = l-1, u+1
                longest = max(longest, (l,u), key=lambda p: p[1]-p[0])
        return s[longest[0]:longest[1]]
                    
            


def test_A0():
    txt = "babad"
    res = Solution().longestPalindrome(txt)
    assert len(res) == 3
    assert check_palindrome(res)
    assert res in txt

def test_A1():
    txt = "a"
    res = Solution().longestPalindrome(txt)
    assert len(res) == 1
    assert check_palindrome(res)
    assert res in txt

def test_A2():
    txt = "a" * 10000
    res = Solution().longestPalindrome(txt)
    assert len(res) == 10000
    assert check_palindrome(res)
    assert res in txt
