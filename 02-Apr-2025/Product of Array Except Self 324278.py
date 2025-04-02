# Problem: Product of Array Except Self - https://leetcode.com/problems/product-of-array-except-self/

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        result = [math.prod(nums)] * length
        for i in range(length):
            if nums[i] != 0:
                result[i] //= nums[i]
            else:
                result[i] = math.prod(nums[:i] + nums[i+1:])
        return result
        