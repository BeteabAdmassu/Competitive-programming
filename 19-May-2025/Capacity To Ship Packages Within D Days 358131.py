# Problem: Capacity To Ship Packages Within D Days - https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/

class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left = max(weights)
        right = sum(weights)
    
        while left < right:
            mid = (left + right) // 2
            current_load = 0
            required_days = 1
        
            for weight in weights:
                if current_load + weight > mid:
                    required_days += 1
                    current_load = 0
                current_load += weight
        
            if required_days <= days:
                right = mid
            else:
                left = mid + 1
    
        return left
        