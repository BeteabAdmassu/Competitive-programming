# Problem: Majority Element - https://leetcode.com/problems/majority-element/description/

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hashmap = Counter(nums)
        for key, value in hashmap.items():
            if value > len(nums) / 2:
                return key
   
        