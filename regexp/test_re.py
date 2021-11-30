
class SolutionTroll:
    def isMatch(self, s: str, p: str) -> bool:
        def parse_pattern(p):
            prev = None
            tokens = []
            for x in p:
                if x == '*':
                    if prev == '*':
                        raise Exception('Invalid pattern')
                    tokens.append( (prev, '*') )
                    prev = None
                else:
                    if prev is not None:
                        tokens.append( (prev, None) )
                    prev = x
            if prev is not None:
                tokens.append( (prev, None) )

            return tokens


        def match(s, tokens):
            #print(f'"{s}" {tokens}')
            i = 0
            j = 0
            while j < len(tokens):
                if tokens[j][1] is None:
                    if tokens[j][0] != '.' and (i >= len(s) or tokens[j][0] != s[i]):
                        return False
                    i += 1
                    j += 1
                elif tokens[j][1] == '*':
                    while i < len(s) and (tokens[j][0] == '.' or tokens[j][0] == s[i]):
                        if match(s[i:], tokens[j+1:]):
                            return True
                        i += 1
                    j += 1
                else:
                    raise Exception('Invalid pattern')
            
            return i == len(s) and j == len(tokens)


        return match(s, parse_pattern(p))

class Solution:

    def expand_epsilons(self, states, tokens):
        frontier = states
        reached = states
        while frontier:
            new_frontier = set()
            for s in frontier:
                if s < len(tokens) and tokens[s][1] == '*':
                    new_frontier.add(s+1)
            frontier = new_frontier.difference(reached)
            reached = reached.union(frontier)

        return reached

    def parse_pattern(self, p):
        prev = None
        tokens = []
        for x in p:
            if x == '*':
                if prev == '*':
                    raise Exception('Invalid pattern')
                tokens.append( (prev, '*') )
                prev = None
            else:
                if prev is not None:
                    tokens.append( (prev, None) )
                prev = x
        if prev is not None:
            tokens.append( (prev, None) )

        return tokens                         
    
    def isMatch(self, s: str, p: str) -> bool:

        tokens = self.parse_pattern(p)
        current_states = self.expand_epsilons({0}, tokens)

        for c in s:
            new_states = set()
            for s in current_states:
                if s < len(tokens):
                    t0, t1 = tokens[s]
                    if t0 == '.' or t0 == c:
                        new_states.add(s+(1 if t1 is None else 0))

            current_states = self.expand_epsilons(new_states, tokens)

        return len(tokens) in current_states




def test_A0():
    assert Solution().isMatch("", "b*") == True
    assert Solution().isMatch("a", "ab*") == True

    assert Solution().isMatch("aa", "a*") == True

    assert Solution().isMatch("mississippi", "mis*is*p*.") == False
    assert Solution().isMatch("aa", "a") == False
    assert Solution().isMatch("aa", "aa") == True
    assert Solution().isMatch("aaa", "aa") == False
    assert Solution().isMatch("aa", ".*") == True
    assert Solution().isMatch("ab", ".*") == True
    assert Solution().isMatch("aab", "c*a*b") == True


def test_epsilon():

    assert Solution().expand_epsilons({0}, [('a', '*')]) == {0,1}
    assert Solution().expand_epsilons({0}, [('a', '*'), ('a', '*')]) == {0,1,2}
    assert Solution().expand_epsilons({0}, [('a', '*'), ('a', None)]) == {0,1}


