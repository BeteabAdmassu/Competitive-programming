# Problem: Unique Paths II - https://leetcode.com/problems/unique-paths-ii/

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        a = len(obstacleGrid)
        b = len(obstacleGrid[0])

        d = [[0] * b for _ in range(a)]
        if obstacleGrid[a-1][b-1] != 1:
            d[a-1][b-1] = 1

        for i in range(a-1, -1, -1):
            for j in range(b-1, -1, -1):
                if i == a-1 and j == b-1:
                    continue
                elif obstacleGrid[i][j] != 1:
                    if i + 1 >= a:
                        d[i][j] = d[i][j+1]
                    elif j + 1 >= b:
                        d[i][j] = d[i+1][j]
                    else:
                        d[i][j] = d[i+1][j] + d[i][j+1]
                else:
                    d[i][j] = 0
        return d[0][0]
