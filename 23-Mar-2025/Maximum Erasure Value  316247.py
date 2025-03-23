# Problem: Maximum Erasure Value  - https://leetcode.com/problems/maximum-erasure-value/

class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        
        left, right = 0 , 0

        unique = set()
        score = 0
        max_score = 0

        while right < len(nums) and left <= right:

            if nums[right] not in unique:
                unique.add(nums[right])
                score += nums[right]
                right += 1
                max_score = max(max_score, score)
            else:
                unique.remove(nums[left])
                score -= nums[left]
                left += 1
            
        return max_score