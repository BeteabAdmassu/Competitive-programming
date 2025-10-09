# Problem: Minimum Cost to Convert String I - https://leetcode.com/problems/minimum-cost-to-convert-string-i/description/?envType=problem-list-v2&envId=shortest-path

class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        def dijkstra(start_node):
            costs = defaultdict(lambda: inf)
            processed = set()
            costs[start_node] = 0

            heap = [(0, start_node)]
            while heap:
                cost, node = heappop(heap)

                if node in processed:
                    continue
                
                processed.add(node)
                for child, weight in graph[node]:
                    dist = cost+weight
                    if dist < costs[child]:
                        costs[child] = dist
                        heappush(heap, (dist, child))
            
            return dict(costs)

        graph = defaultdict(list)
        for a, b, c in zip(original, changed, cost):
            graph[a].append((b, c))

        costs = {}
        for node in set(original):
            csts = dijkstra(node)
            csts[node] = 0
            costs[node] = csts
        
        ans = 0
        for c1, c2 in zip(source, target):
            if c1 == c2:
                continue
            if c1 not in costs:
                return -1
            if c2 not in costs[c1]:
                return -1
            ans += costs[c1][c2]
        
        return ans