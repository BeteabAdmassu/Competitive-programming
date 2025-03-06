# Problem: Squares of a Sorted Array
(Easy) - https://leetcode.com/problems/squares-of-a-sorted-array/

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        arr = [i**2 for i in nums]
        arr.sort() 
        return arr

        


        