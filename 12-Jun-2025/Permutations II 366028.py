# Problem: Permutations II - https://leetcode.com/problems/permutations-ii/description/

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        used = [False] * len(nums)
        self.backtrack(nums, used, [], result)
        return result
    
    def backtrack(self, nums, used, path, result):
        if len(path) == len(nums):
            result.append(path.copy())
            return
        for i in range(len(nums)):
            if used[i] or (i > 0 and nums[i] == nums[i-1] and not used[i-1]):
                continue
            used[i] = True
            path.append(nums[i])
            self.backtrack(nums, used, path, result)
            used[i] = False
            path.pop()
        