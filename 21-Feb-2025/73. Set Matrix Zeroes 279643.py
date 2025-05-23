# Problem: 73. Set Matrix Zeroes - https://leetcode.com/problems/set-matrix-zeroes/description/

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """


        col = set()
        row = set()
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    col.add(i)
                    row.add(j)

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i in col or j in row:
                    matrix[i][j] = 0
               


        
