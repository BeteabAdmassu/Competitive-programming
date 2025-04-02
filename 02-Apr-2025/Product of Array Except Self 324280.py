# Problem: Product of Array Except Self - https://leetcode.com/problems/product-of-array-except-self/

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        res = [math.prod(nums)] * length
        for i in range(length):
            if nums[i] != 0:
                res[i] //= nums[i]
            else:
                res[i] = math.prod(nums[:i] + nums[i+1:])
        return res
        