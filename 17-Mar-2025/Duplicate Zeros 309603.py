# Problem: Duplicate Zeros - https://leetcode.com/problems/duplicate-zeros/description/?envType=problem-list-v2&envId=two-pointers

class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """

        #brute force
        left, right = 0 , len(arr) - 1

        while left < len(arr):
            if arr[left] == 0:
                while right > left:
                    arr[right] = arr[right - 1]
                    right -= 1
                right = len(arr) - 1
                left += 2
            else:
                left += 1

