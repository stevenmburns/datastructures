class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        x, y = 0, 0
        Ss = "NWSE"
        Ls = Ss[1:] + Ss[:1]
        Rs = Ss[:1] + Ss[1:]

        ds = {"N": (0, 1), "W": (-1, 0), "S": (0, -1), "E": (1, 0)}

        def LL(d):
            return Ls[Ss.index(d)]

        def RR(d):
            return Rs[Ss.index(d)]

        d = 'N'
        for c in instructions:
            if c == 'G':
                dx, dy = ds[d]
                x, y = x + dx, y + dy
            elif c == 'L':
                d = LL(d)
            elif c == 'R':
                d = RR(d)
            else:
                assert False, c

        return (x, y) == (0, 0) or d in "WSE"


def test_A0():
    assert Solution().isRobotBounded("GGLLGG")


def test_A1():

    assert not Solution().isRobotBounded("GG")


def test_A2():

    assert Solution().isRobotBounded("GL")
