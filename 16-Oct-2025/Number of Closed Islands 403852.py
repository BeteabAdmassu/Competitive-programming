# Problem: Number of Closed Islands - https://leetcode.com/problems/number-of-closed-islands/


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
    def closedIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        uf = UnionFind(rows * cols)

        dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        for row in range(rows):
            temp = -1
            for col in range(cols):
                if grid[row][col] == 0:
                    index = row * cols + col
                    for dr, dc in dirs:
                        r, c = row + dr, col + dc
                        if 0 <= r < rows and 0 <= c < cols and grid[r][c] == 0:
                            uf.union(index, r * cols + c)

        edges = set()
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 0:
                    if row == 0 or row == rows-1 or col == 0 or col == cols - 1:
                        parent = uf.find(row * cols + col)
                        edges.add(parent)

        closed = set()
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 0:
                    parent = uf.find(row * cols + col)
                    if parent not in edges:
                        closed.add(parent)

        return len(closed)