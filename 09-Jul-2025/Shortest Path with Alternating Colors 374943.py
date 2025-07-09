# Problem: Shortest Path with Alternating Colors - https://leetcode.com/problems/shortest-path-with-alternating-colors/description/

class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        red = defaultdict(list)
        blue = defaultdict(list)

        for i, j in redEdges:
            red[i].append(j)

        for i, j in blueEdges:
            blue[i].append(j)

        res = [-1 for _ in range(n)]
        queue = deque()
        queue.append([0, 0, None])
        visited = set()
        visited.add((0, None))

        while queue:
            node, length, color = queue.popleft()
            if res[node] == -1:
                res[node] = length

            if color != "red":
                for x in red[node]:
                    if (x, "red") not in visited:
                        visited.add((x, "red"))
                        queue.append([x, length+1, "red"])

            if color != "blue":
                for x in blue[node]:
                    if (x, "blue") not in visited:
                        visited.add((x, "blue"))
                        queue.append([x, length+1, "blue"])

        return res
        