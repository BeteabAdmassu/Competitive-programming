# Problem: Map of Highest Peak - https://leetcode.com/problems/map-of-highest-peak/description/

class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        queue = deque()
        visited = set()
        res = [[-1] * len(isWater[0]) for _ in range(len(isWater))]

        for i in range(len(isWater)):
            for j in range(len(isWater[0])):
                if isWater[i][j]:
                    queue.append((i, j))
                    visited.add((i, j))
                    res[i][j] = 0

        while queue:
            i, j = queue.popleft()
            count = res[i][j]

            adj = [[i+1, j], [i, j+1], [i-1, j], [i, j-1]]
            for x, y in adj:
                if (x < 0 or y < 0 or x == len(isWater) or y == len(isWater[0]) or res[x][y] != -1):
                    continue 
                queue.append((x, y))
                res[x][y] = count + 1
        return res