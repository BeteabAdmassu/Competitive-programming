# Problem: Build Array from Permutation - https://leetcode.com/problems/build-array-from-permutation/description/

class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        p = [0] * len(nums)

        for i in range(len(nums)):
            p[i] = nums[nums[i]]

        return p

        