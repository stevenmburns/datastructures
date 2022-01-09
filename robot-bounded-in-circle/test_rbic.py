class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        x, y = 0,0
        dx, dy = 0,1
        Ss = "NWSE"
        Ls = Ss[1:] + Ss[:1]
        Rs = Ss[:1] + Ss[1:]

        ds = { "N" : (0,1), "W": (-1,0), "S": (0,-1), "E": (1,0)}
        inv_ds = { v: k for k,v in ds.items()}

        def LL(d):
            return ds[Ls[Ss.index(inv_ds[d])]]

        def RR(d):
            return ds[Rs[Ss.index(inv_ds[d])]]

        L = { (0,1): (-1, 0), (-1,0): (0, -1), (0, -1): (1, 0), (1,0) : (0, 1)}
        R = { (0,1): (1, 0), (1,0): (0, -1), (0, -1): (-1, 0), (-1,0) : (0, 1)}



        for c in instructions  * 4:
            if c == 'G':
                x, y = x + dx, y + dy
            elif c == 'L':
                dx, dy = LL((dx,dy))
            elif c == 'R':
                dx, dy = RR((dx,dy))
            else:
                assert False, c

        return (x,y) == (0,0)


def test_A0():
    assert Solution().isRobotBounded("GGLLGG")
def test_A1():

    assert not Solution().isRobotBounded("GG")
def test_A2():

    assert Solution().isRobotBounded("GL")