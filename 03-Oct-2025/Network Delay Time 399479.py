# Problem: Network Delay Time - https://leetcode.com/problems/network-delay-time/description/

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for u, v, w in times:
            graph[u].append((v,w))
        
        distances = [float('inf')] * (n+1)
        processed = set()
        distances[0] = 0

        total = 0

        heap = [(0, k)]
        while heap:
            cost, curr = heapq.heappop(heap)
            if curr in processed:
                continue
            processed.add(curr)
            distances[curr] = cost

            for neighbor, weight in graph[curr]:
                if cost + weight < distances[neighbor]:
                    distances[neighbor] = cost + weight
                    heapq.heappush(heap, (cost + weight, neighbor))
        
        return max(distances) if max(distances) != float('inf') else -1
