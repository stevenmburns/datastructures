import random

def compute_cost( dims):
    """
    (5 x 2) (2 x 7) (7 x 9)
    
    costs[(0,1)] = 0
    costs[(1,2)] = 0
    costs[(2,3)] = 0

    costs[(0,2)] = costs[(0,1)] + (5*2*7) + costs[(1,2)] = 5*2*7
    costs[(1,3)] = costs[(1,2)] + (2*7*9) + costs[(2,3)] = 2*7*9

    costs[(0,3)] = min(costs[(0,1)] + (5*2*9) + costs[(1,3)],
                       costs[(0,2)] + (5*7*9) + costs[(2,3)])
                 = min(0 + 5*2*9 + 2*7*9, 5*2*7 + 5*7*9 + 0)
"""

    costs = {}
    
    for i in range(len(dims)):
        costs[(i,i+1)] = 0

    for j in range(1,len(dims)):
        for i in range(len(dims)-j):
            ii = i + j + 1
            costs[(i,ii)] = min(costs[(i,k)] + dims[i][0]*dims[k][0]*dims[ii-1][1] + costs[(k,ii)] for k in range(i+1,ii))

    return costs[(0,len(dims))]

def test_A():
    """
    (5 x 2) (2 x 7) (7 x 9)
"""
    x = [(5,2),(2,7),(7,9)]                                                     
    #assert compute_cost(x) == (5 * 2 * 7) + (5 * 7 * 9)
    assert compute_cost(x) == (5 * 2 * 9) + (2 * 7 * 9)

    pass

def test_B():
    random.seed(47)
    dims = [random.randrange(1,100) for _ in range(200)]
    sizes = list(zip(dims[:-1],dims[1:]))
    print(dims)
    print(sizes)
    assert compute_cost(sizes) == 502262
