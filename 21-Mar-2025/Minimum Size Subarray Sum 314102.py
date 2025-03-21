# Problem: Minimum Size Subarray Sum - https://leetcode.com/problems/minimum-size-subarray-sum/

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

   
        
        left , right = 0 , 1
        count = 0
        _sum = nums[left]

        if len(nums) < 2:
            if _sum > target:
                return 1
            return 0

            
        while left <= right and right < len(nums):
            if _sum > target:
                count = 1
                left += 1
                right += 1
                continue
                
            _sum += nums[right]

            if _sum >= target:
                if count == 0:
                    count = len(nums[left:right + 1])
                else:
                    count = min(count, len(nums[left:right + 1]) )
            
                _sum -= nums[left]
                _sum -= nums[right]
                left += 1
            
            else:
                right += 1  
          

        return count

        
            
        