# Problem: Accounts Merge - https://leetcode.com/problems/accounts-merge/

class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX == rootY:
            return
        if rootX < rootY:
            self.parent[rootY] = rootX
        else:
            self.parent[rootX] = rootY

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        email_track = {}
        name_track = {}
        count = 0
        for acc in accounts:
            for i in range(1, len(acc)):
                if acc[i] not in email_track:
                    email_track[acc[i]] = count
                    name_track[acc[i]] = acc[0]
                    count += 1
        uf = UnionFind(count)
        for i in range(len(accounts)):
            x = accounts[i][1]
            for email in accounts[i][2:]:
                uf.union(email_track[x], email_track[email])
        
        parent_track = defaultdict(list)
        for key, value in email_track.items():
            parent = uf.find(value)
            parent_track[parent].append(key)

        res = []

        for emails in parent_track.values():
            name = name_track[emails[0]]
            res.append([name] + sorted(emails))


        return res