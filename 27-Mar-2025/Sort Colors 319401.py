# Problem: Sort Colors - https://leetcode.com/problems/sort-colors/

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.

        """

        red = 0
        white = 0
        blue = len(nums) - 1
        
        while white <= blue:
            if nums[white] == 0:
                nums[white], nums[red] = nums[red], nums[white]
                red += 1
                white += 1
            elif nums[white] == 1:
                white += 1
            else:
                nums[white], nums[blue] = nums[blue], nums[white]
                blue -= 1



        # BruteForce soultion
        # for i in range(len(nums) - 1):
        #     for j in range(i ,len(nums)):
        #         if nums[i] > nums[j]:
        #             nums[i], nums[j] = nums[j],nums[i]




        