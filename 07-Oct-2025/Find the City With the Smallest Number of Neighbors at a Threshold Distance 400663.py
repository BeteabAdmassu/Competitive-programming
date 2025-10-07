# Problem: Find the City With the Smallest Number of Neighbors at a Threshold Distance - https://leetcode.com/problems/find-the-city-with-the-smallest-number-of-neighbors-at-a-threshold-distance/

class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        dist: list[list[int]] = [[float("inf") for _ in range(n)] for _ in range(n)]
        for i in range(n):
            dist[i][i] = 0

        for u, v, w in edges:
            dist[u][v] = w
            dist[v][u] = w

        for mid in range(n):
            for src in range(n):
                for dst in range(n):
                    dist[src][dst] = min(dist[src][dst], dist[src][mid] + dist[mid][dst])  

        mini_num: int = n
        res: int = None

        for src in range(n):
            src_count = 0
            for dst in range(n):
                if dist[src][dst] <= distanceThreshold:
                    src_count += 1

            if src_count <= mini_num:
                mini_num = src_count
                res = src

        return res
            

            

