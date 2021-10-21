from itertools import accumulate

class Tree:
    def __init__(self, key, l=None, r=None):
        self.key = key
        self.l = l
        self.r = r

    def __eq__(self, other):
        return other is not None and self.key == other.key and self.l == other.l and self.r == other.r

    def find(self, key):
        if key == self.key:
            return self
        elif key < self.key:
            if self.l is not None:
                return self.l.find(key)
            else:
                return None
        else:
            if self.r is not None:
                return self.r.find(key)
            else:
                return None
            if self.l is not None:
                return self.l.find(key)
            else:
                return None

    @staticmethod
    def build(keys, probs):
        
        cprobs = (0,) + tuple(accumulate(probs))

        assert len(keys) == len(probs)

        assert keys == list(sorted(keys))

        costs = {}
        for i in range(len(keys)+1):
            # (0,0),(1,1),(2,2),(3,3)
            costs[(i,i)] = 0, None

        for i in range(len(keys)):
            # (0,1),(1,2),(2,3)
            costs[(i,i+1)] = probs[i], i

        # j in {1,2}
        for j in range(1,len(keys)):
            # i in {0,1} for j == 1
            # i in {0}   for j == 2
            for i in range(len(keys)-j):
                #    (0,2),(1,3)
                #       (0,3)
                ii = i + j + 1
                # for (0,2) we need (0,0) 0 (1,2); (0,1) 1 (2,2)

                # probs =  0.3 0.2 0.5
                # keys  =  0   1   2   3  
                # cprobs:  0.0 0.3 0.5 1.0
                # probs between (0,2) cprob[2] - cprob[0]
                # probs[k] = cprobs[k+1] - cprobs[k]

                lst = []
                for k in range(i,ii):
                    cand2 = costs[(i,k)][0]    + cprobs[k]  - cprobs[i]   + \
                            costs[(k+1,ii)][0] + cprobs[ii] - cprobs[k+1] + \
                            probs[k]
                    cand = costs[(i,k)][0]    - cprobs[i]   + \
                           costs[(k+1,ii)][0] + cprobs[ii]
                    assert abs(cand - cand2) <= 0.00001
                        
                    lst.append( (cand, k))
                costs[(i,ii)] = min(lst)
                
        def aux(lb, ub):
            if lb < ub:
                _, k = costs[(lb,ub)]
                return Tree(k, aux(lb, k), aux(k+1, ub))
            else:
                return None

        print(costs[(0,len(keys))])

        return aux(0,len(keys))

    def __repr__(self):
        return f'Tree({self.key}, {repr(self.l)}, {repr(self.r)})'

def test_A():
    t = Tree(1, Tree(0), Tree(2)) 
    for x in range(3):
        assert t.find(x) is not None

def test_B():

    t = Tree.build( [0], [1.0])
    assert t == Tree(0)

    t = Tree.build( [0,1], [.3,.7])
    assert t == Tree(1, Tree(0), None)

    t = Tree.build( [0,1], [.7,.3])
    assert t == Tree(0, None, Tree(1))

    t = Tree.build( [0,1,2], [.3,.2,.5])
    assert t == Tree(2, Tree(0, None, Tree(1)))
