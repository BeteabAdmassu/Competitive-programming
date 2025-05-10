# Problem: Search a 2D Matrix - https://leetcode.com/problems/search-a-2d-matrix/

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for row in matrix:
            if target > row[-1]:
                continue
            left, right = 0, len(row)-1
            while left <= right:
                if left == right:
                    return target == row[left]
                mid = (left+right)//2
                if row[mid] == target:
                    return True
                elif row[mid] < target:
                    left = mid+1
                else:
                    right = mid
            
            return False
        return False
        