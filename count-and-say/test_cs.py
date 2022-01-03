class Solution:
    def countAndSay(self, n: int) -> str:
        def reps(s):
            count = 0
            pairs = []

            for c in s:
                if count > 0 and last != c:
                    pairs.append((count, last))
                    count = 0
                count += 1
                last = c

            if count > 0:
                pairs.append((count, last))

            return pairs

        s = '1'
        for _ in range(n-1):
            s = ''.join(f'{p[0]}{p[1]}' for p in reps(s))
        return s


def test_A0():
    assert Solution().countAndSay(1) == '1'
    assert Solution().countAndSay(4) == '1211'
