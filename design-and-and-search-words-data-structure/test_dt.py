class WordDictionaryAcceptable:

    def __init__(self):
        self.t = {}

    def addWord(self, word: str) -> None:
        t = self.t
        for c in word:
            if c not in t:
                t[c] = {}
            t = t[c]
        t['$'] = {}

    def search(self, word: str) -> bool:
        def aux(t, w):
            while True:
                c, neww = w[0], w[1:]
                if c == '$':
                    return c in t
                elif c == '.':
                    return any(aux(tt, neww) for _, tt in t.items())
                elif c in t:
                    t, w = t[c], neww
                else:
                    return False

        return aux(self.t, word + '$')


class WordDictionary:

    def __init__(self):
        self.t = {}

    def addWord(self, word: str) -> None:
        t = self.t
        for c in word:
            if c not in t:
                t[c] = {}
            t = t[c]
        t['$'] = {}

    def search(self, word: str) -> bool:
        def aux(t, j):
            while True:
                if j == len(word):
                    return '$' in t
                else:
                    c = word[j]
                    if c == '.':
                        return any(aux(tt, j+1) for _, tt in t.items())
                    elif c in t:
                        t, j = t[c], j+1
                    else:
                        return False

        return aux(self.t, 0)


def test_A0():
    cmds = ["WordDictionary", "addWord", "addWord", "addWord", "addWord", "search",
            "search", "addWord", "search", "search", "search", "search", "search", "search"]
    args = [
        [],
        ["at"],
        ["and"],
        ["an"],
        ["add"],
        ["a"],
        [".at"],
        ["bat"],
        [".at"],
        ["an."],
        ["a.d."],
        ["b."],
        ["a.d"],
        ["."]]
    results = [None, None, None, None, None, False, False, None, True, True, False, False, True, False]

    wd = WordDictionary()

    for cmd, arg, result in zip(cmds, args, results):
        if cmd == "WordDictionary":
            wd = WordDictionary()
        elif cmd == "addWord":
            wd.addWord(arg[0])
        elif cmd == "search":
            assert wd.search(arg[0]) == result, (cmd, arg, result)
        else:
            raise Exception(f"Unknown command: {cmd}")
