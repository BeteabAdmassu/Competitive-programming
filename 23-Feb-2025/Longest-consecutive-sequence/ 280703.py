# Problem: Longest-consecutive-sequence/ - https://leetcode.com/problems/longest-consecutive-sequence/

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
           
        if len(nums) < 2: 
            return len(nums) 

        numsSet = set(nums)
        count = 0
        for num in numsSet:
            if num - 1 not in numsSet:
                current_num = num
                current_streak = 1

                while current_num + 1 in numsSet:
                    current_num += 1
                    current_streak += 1

                count = max(count, current_streak)

        return count
                

            