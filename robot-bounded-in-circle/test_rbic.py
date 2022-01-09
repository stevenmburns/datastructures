class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        ds = [(0, 1), (-1, 0), (0, -1), (1, 0)]
        x, y = 0, 0
        d = 0
        for c in instructions:
            if c == 'G':
                dx, dy = ds[d]
                x, y = x + dx, y + dy
            elif c == 'L':
                d = (d + 1) % 4
            elif c == 'R':
                d = (d - 1) % 4
            else:
                assert False, c
        return (x, y) == (0, 0) or d != 0


def test_A0():
    assert Solution().isRobotBounded("GGLLGG")


def test_A1():

    assert not Solution().isRobotBounded("GG")


def test_A2():

    assert Solution().isRobotBounded("GL")
