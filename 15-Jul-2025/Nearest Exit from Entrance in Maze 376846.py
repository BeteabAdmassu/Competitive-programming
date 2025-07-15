# Problem: Nearest Exit from Entrance in Maze - https://leetcode.com/problems/nearest-exit-from-entrance-in-maze/

class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        m = len(maze)
        n = len(maze[0])

        queue = deque()
        visited = set()

        visited.add((entrance[0], entrance[1]))
        queue.append((entrance[0], entrance[1], 0))
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        while queue:
            x, y, steps = queue.popleft()
            for d in directions:
                next_x = d[0] + x
                next_y = d[1] + y
                if 0 <= next_x < m and 0 <= next_y < n:
                    if (next_x, next_y) not in visited and maze[next_x][next_y] == '.':
                        if next_x == m-1 or next_x == 0 or next_y == n-1 or next_y == 0:
                            return steps+1
                        queue.append((next_x, next_y, steps+1))
                        visited.add((next_x, next_y))
        return -1
        