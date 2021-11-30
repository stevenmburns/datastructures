
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

        tokens = []
        for x in p:
            if x == '*':
                tokens.append(('.', '*'))
            elif x == '?':
                tokens.append(('.', None))
            else:
                tokens.append((x, None))  
        return tokens                     
    
    def isMatch(self, s: str, p: str) -> bool:


        def squash(p):
            result = []
            i = 0
            prev = None
            for x in p:
                if x == '*' and prev == '*':
                    pass
                else:
                    result.append(x)
                prev = x
                
            return ''.join(result)

        tokens = self.parse_pattern(squash(p))

        current_states = self.expand_epsilons({0}, tokens)

        for c in s:
            new_states = set()
            for s in current_states:
                if s < len(tokens):
                    if tokens[s][1] is None:
                        if tokens[s][0] == '.' or tokens[s][0] == c:
                            new_states.add(s+1)
                    elif tokens[s][1] == '*':
                        if tokens[s][0] == '.' or tokens[s][0] == c:
                            new_states.add(s)

            current_states = self.expand_epsilons(new_states, tokens)

        return len(tokens) in current_states




def test_A0():
    """Test wildcard matching"""


    assert Solution().isMatch("", "*") == True
    assert Solution().isMatch("", "?") == False
    assert Solution().isMatch("", "") == True
    assert Solution().isMatch("b", "b*") == True
    assert Solution().isMatch("b", "b?") == False
    assert Solution().isMatch("aa", "*") == True

def test_A1():

    s = "babbbbaabababaabbababaababaabbaabababbaaababbababaaaaaabbabaaaabababbabbababbbaaaababbbabbbbbbbbbbaabbb"
    p = "b**bb**a**bba*b**a*bbb**aba***babbb*aa****aabb*bbb***a"

    assert Solution().isMatch(s, p) == False


