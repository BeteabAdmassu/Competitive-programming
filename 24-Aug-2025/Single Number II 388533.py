# Problem: Single Number II - https://leetcode.com/problems/single-number-ii/

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums.sort()
        i = 0
        while i < len(nums)-2:
            if nums[i] ^ nums[i+1] == 0 and nums[i+1] ^ nums[i+2] == 0:
                i += 3
            else:
                return nums[i]
        return nums[i]