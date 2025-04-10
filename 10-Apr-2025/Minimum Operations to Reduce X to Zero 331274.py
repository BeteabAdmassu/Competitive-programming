# Problem: Minimum Operations to Reduce X to Zero - https://leetcode.com/problems/minimum-operations-to-reduce-x-to-zero/description/

class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        left = 0
        right = 0
        
        t = sum(nums) - x



        maximum = -1
        flag = False
        value = 0
        while right < len(nums) and left < len(nums):

            value += nums[right]
            while left <= right and value > t: 
                value -= nums[left]
                left += 1
                
        
            if value == t:
                maximum = max(maximum,  (right - left) + 1 )
                
                flag = True
            right += 1
        
            print(value)
        if maximum == -1:
            return maximum
        return len(nums) - maximum

        