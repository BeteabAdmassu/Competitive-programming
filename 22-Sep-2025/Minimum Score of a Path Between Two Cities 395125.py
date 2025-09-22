# Problem: Minimum Score of a Path Between Two Cities - https://leetcode.com/problems/minimum-score-of-a-path-between-two-cities/description/

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
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        uf = UnionFind(n+1)
        for road in roads:
            a, b, dist = road
            uf.union(a, b)
        
        min_score = float('inf') 
        parent1 = uf.find(1)
        for road in roads:
            a, b, dist = road
            if uf.find(a) == parent1 or uf.find(b) == parent1:
                min_score = min(min_score, dist)
        
        return min_score