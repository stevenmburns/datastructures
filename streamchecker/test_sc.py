
from typing import List

from collections import defaultdict

class StreamChecker:

    def __init__(self, words: List[str]):

        self.states = []
        assert words == ["cd", "f", "kl"]


        def build( lst):
            first_chars = defaultdict(list)
            trie = {}
            for word in lst:
                first_chars[word[0]].append(word[1:])
            for k, v in first_chars.items():
                is_final = any( len(word) == 0 for word in v)
                vv = [word for word in v if len(word) > 0]
                trie[k] = (is_final, build(vv))
            return trie

        self.trie = build(words)
        if False:
            self.trie = { 'c': (False, {'d': (True, None)}),
                        'f': (True, None),
                        'k': (False, {'l': (True, None)})
                        }   

    def query(self, letter: str) -> bool:

        self.states.append( self.trie)
        result = False

        next_states = []

        for state in self.states:
            if letter in state:
                is_final, next_state = state[letter]
                if next_state is not None:
                    next_states.append(next_state)
                result = result or is_final
        
        self.states = next_states
        return result




def test_A0():
    s = StreamChecker(["cd","f","kl"])
    assert s.query('a') == False
    assert s.query('b') == False
    assert s.query('c') == False
    assert s.query('d') == True
    assert s.query('e') == False
    assert s.query('f') == True
    assert s.query('g') == False
    assert s.query('h') == False
    assert s.query('i') == False
    assert s.query('j') == False
    assert s.query('k') == False
    assert s.query('l') == True