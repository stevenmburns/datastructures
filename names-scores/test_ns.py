def test_A():
    with open("p022_names.txt") as fp:
        names = fp.readline().strip('"').split('","')
        names.sort()
        s = 0
        for idx, name in enumerate(names):
            s += sum(ord(c) - ord('A') + 1 for c in name) * (idx + 1)
        print(s)
