# Problem: Single Number III - https://leetcode.com/problems/single-number-iii/

class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        res = []
        nums.sort()
        i = 0
        while i < len(nums) - 1:
            if nums[i] ^ nums[i+1] == 0:
                i += 2
            else:
                res.append(nums[i])
                i += 1
        if len(res) < 2:
            res.append(nums[-1])
        return res