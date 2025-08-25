# Problem: Subsets - https://leetcode.com/problems/subsets/

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        n = len(nums)

        for i in range(1 << n):
            temp = []
            for j in range(n):
                if i & (1 << j):
                    temp.append(nums[j])
            result.append(temp)
        
        return result