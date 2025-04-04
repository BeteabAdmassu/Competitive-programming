# Problem: Count the Number of Good Subarrays - https://leetcode.com/problems/count-the-number-of-good-subarrays/description/

class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        goodSubarrays = 0
        left = 0
        freq = defaultdict(int)

        for right in range(len(nums)):
            k -= freq[nums[right]]
            freq[nums[right]] += 1

            while k <= 0:
                freq[nums[left]] -= 1
                k += freq[nums[left]]
                left += 1

            goodSubarrays += left

        return goodSubarrays
        