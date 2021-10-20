
def compute_cost( dims):
    """
    (5 x 2) (2 x 7) (7 x 9)
    
    costs[(0,0)] = 0
    costs[(1,1)] = 0
    costs[(2,2)] = 0

    costs[(0,1)] = costs[(0,0)] + (5*2*7) + costs[(1,1)] = 5*2*7
    costs[(1,2)] = costs[(1,1)] + (2*7*9) + costs[(2,2)] = 2*7*9

    costs[(0,2)] = min( costs[(0,0)] + (5*2*9) + costs[(1,2)],
                        costs[(0,1)] + (5*7*9) + costs[(2,2)])
                 = min( 0 + 5*2*9 + 2*7*9,
                        5*2*7 + 5*7*9 + 0)
"""

    costs = {}
    
    for i in range(len(dims)):
        costs[(i,i)] = 0

    for j in range(1,len(dims)):
        for i in range(len(dims)-j):
            ii = i + j
            costs[(i,ii)] = min(costs[(i,k)] + costs[(k+1,ii)] + dims[i][0]*dims[k][1]*dims[ii][1] for k in range(i,ii))

    return costs[(0,len(dims)-1)]

def test_A():
    """
    (5 x 2) (2 x 7) (7 x 9)
"""
    x = [(5,2),(2,7),(7,9)]                                                     
    #assert compute_cost(x) == (5 * 2 * 7) + (5 * 7 * 9)
    assert compute_cost(x) == (5 * 2 * 9) + (2 * 7 * 9)

    pass
