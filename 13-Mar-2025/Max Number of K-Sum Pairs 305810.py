# Problem: Max Number of K-Sum Pairs - https://leetcode.com/problems/max-number-of-k-sum-pairs/

class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        left , right = 0 , len(nums) - 1
        count = 0

        while left < right:
            if nums[left] + nums[right] == k:
                count += 1

                left += 1
                right -= 1
            else:
                if nums[left] + nums[right] > k:
                    right -= 1
                else:
                    left += 1
        return count