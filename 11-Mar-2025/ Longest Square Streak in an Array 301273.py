# Problem:  Longest Square Streak in an Array - https://leetcode.com/problems/longest-square-streak-in-an-array/description/?envType=problem-list-v2&envId=sorting

class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        nums.sort()
        nums_set = set(nums)
        max_streak = 0
        
        for num in nums:
            current_streak = 1
            current_num = num
            
            while current_num ** 2 in nums_set:
                current_streak += 1
                current_num = current_num ** 2
            
            max_streak = max(max_streak, current_streak)
        
        return max_streak if max_streak >= 2 else -1