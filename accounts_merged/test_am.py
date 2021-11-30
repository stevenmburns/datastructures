from typing import List
from collections import defaultdict


class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [0 for _ in range(n)]

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        x_root = self.find(x)
        y_root = self.find(y)
        if x_root == y_root:
            return
        if self.rank[x_root] < self.rank[y_root]:
            self.parent[x_root] = y_root
        elif self.rank[x_root] > self.rank[y_root]:
            self.parent[y_root] = x_root
        else:
            self.parent[y_root] = x_root
            self.rank[x_root] += 1


class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:

        emails = {}
        
        for account in accounts:
            nm = account[0]
            for email in account[1:]:
                if email not in emails:
                    emails[email] = nm, len(emails)
                else:
                    assert emails[email][0] == nm

        uf = UnionFind(len(emails))
        for account in accounts:
            if len(account) > 2:
                for email in account[2:]:
                    uf.union(emails[email][1], emails[account[1]][1])

        d = defaultdict(list)

        for email, (_, idx) in emails.items():
            d[uf.find(idx)].append(email)


        names = list(emails.values())

        return [[names[k][0]] + list(sorted(v)) for k, v in d.items()]


def test_A0():
    input = [
        ["John","johnsmith@mail.com","john_newyork@mail.com"],
        ["John","johnsmith@mail.com","john00@mail.com"],
        ["Mary","mary@mail.com"],
        ["John","johnnybravo@mail.com"]
    ]

    output = [       
        ["John","johnsmith@mail.com","john_newyork@mail.com","john00@mail.com"],
        ["Mary","mary@mail.com"],
        ["John","johnnybravo@mail.com"]
    ]

    def canonize(lst_of_lsts):
        return sorted(sorted(lst) for lst in lst_of_lsts)


    assert canonize(output) == canonize(Solution().accountsMerge(input))