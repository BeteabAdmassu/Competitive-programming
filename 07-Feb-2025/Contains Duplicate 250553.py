# Problem: Contains Duplicate - https://leetcode.com/problems/contains-duplicate/description/

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        sets = { i for i in nums}
        if len(sets) != len(nums):
            return True
        return False
        