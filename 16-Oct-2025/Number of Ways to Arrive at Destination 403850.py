# Problem: Number of Ways to Arrive at Destination - https://leetcode.com/problems/number-of-ways-to-arrive-at-destination/

class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        adj_list = defaultdict(list)
        for u, v, w in roads:
            adj_list[u].append((w, v))
            adj_list[v].append((w, u))
        
        MOD = 10**9 + 7
        heap = []
        heapq.heappush(heap, (0, 0))
        min_cost = [float('inf')] * n
        counts = [0] * n
        counts[0] = 1

        while heap:
            cost, temp = heapq.heappop(heap)

            for nei_cost, nei in adj_list[temp]:
                if cost + nei_cost < min_cost[nei]:
                    min_cost[nei] = cost + nei_cost
                    counts[nei] = counts[temp]
                    heapq.heappush(heap, (cost + nei_cost, nei))
                elif cost + nei_cost == min_cost[nei]:
                    counts[nei] = (counts[nei] + counts[temp]) % MOD
        return counts[n-1]