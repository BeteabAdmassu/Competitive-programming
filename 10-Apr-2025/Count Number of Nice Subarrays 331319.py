# Problem: Count Number of Nice Subarrays - https://leetcode.com/problems/count-number-of-nice-subarrays/

class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        count = 0
        prefix = defaultdict(int)
        prefix[0] = 1
        odd_count = 0
        
        for num in nums:
            if num % 2 == 1:
                odd_count += 1
            count += prefix[odd_count - k]
            prefix[odd_count] += 1
        
        return count

        