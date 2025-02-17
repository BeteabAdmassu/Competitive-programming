# Problem: Replace Elements in an Array - https://leetcode.com/problems/replace-elements-in-an-array/

class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        index = {i: v for i, v in enumerate(nums)}
        value = {v: i for i, v in enumerate(nums)}

        for operation in operations:
            ix = value[operation[0]]
            index[ix] = operation[1]
            value[operation[1]] = ix 
            del value[operation[0]]

        for i in range(len(nums)):
            nums[i] = index[i]

        return nums

        