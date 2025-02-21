# Problem: Transpose Matrix - https://leetcode.com/problems/transpose-matrix/

class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:

        m, n = len(matrix), len(matrix[0])
        result = [[0] * m for _ in range(n)]
        for row in range(m):
            for col in range(n):
                result[col][row] = matrix[row][col]
        
        return result
        