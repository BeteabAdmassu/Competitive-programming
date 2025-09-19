# Problem: Find Greatest Common Divisor of Array - https://leetcode.com/problems/find-greatest-common-divisor-of-array/

class Solution:
    def findGCD(self, nums: List[int]) -> int:
        max_val = max(nums)
        min_val = min(nums)
        for i in range(min_val, -1, -1):
            if min_val % i == 0 and max_val % i == 0:
                return i
        return 1