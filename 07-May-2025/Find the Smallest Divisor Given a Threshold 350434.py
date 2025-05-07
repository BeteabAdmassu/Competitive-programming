# Problem: Find the Smallest Divisor Given a Threshold - https://leetcode.com/problems/find-the-smallest-divisor-given-a-threshold/

class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        left = 1
        right = max(nums)
        result = right  
    
        while left <= right:
            mid = (left + right) // 2
            sums = 0
            for num in nums:
                sums += math.ceil(num / mid)
        
            if sums <= threshold:
                result = mid
                right = mid - 1  
            else:
                left = mid + 1  
    
        return result
        