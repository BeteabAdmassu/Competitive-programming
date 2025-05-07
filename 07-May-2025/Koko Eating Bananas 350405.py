# Problem: Koko Eating Bananas - https://leetcode.com/problems/koko-eating-bananas/

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        result = right  
    
        while left <= right:
            mid = (left + right) // 2
            hours = 0
            for pile in piles:
                hours += math.ceil(pile / mid)
        
            if hours <= h:
                result = mid
                right = mid - 1  
            else:
                left = mid + 1  
    
        return result
        