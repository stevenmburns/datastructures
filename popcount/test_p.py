
def popcount_silly(x):
    return bin(x).count('1')


def popcount_loop(x):
    count = 0
    while x:
        count += 1
        x &= x - 1
    return count


def popcount_log(x):
    masks = [0x5555555555555555, 0x3333333333333333, 0x0f0f0f0f0f0f0f0f,
             0x00ff00ff00ff00ff, 0x0000ffff0000ffff, 0x00000000ffffffff]
    for idx, mask in enumerate(masks):
        x = (x & mask) + ((x >> (1 << idx)) & mask)
    return x


popcount = popcount_log


def test_A0():
    for popcount in (popcount_silly, popcount_loop, popcount_log):
        assert popcount(0) == 0
        assert popcount(255) == 8
        assert popcount(0x5555555555555555) == 32
        assert popcount(0x3333333333333333) == 32
        assert popcount(0xcccccccccccccccc) == 32
        assert popcount(0x0f0f0f0f0f0f0f0f) == 32
        assert popcount(0xffffffffffffffff) == 64
