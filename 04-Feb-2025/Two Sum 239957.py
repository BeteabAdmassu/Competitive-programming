# Problem: Two Sum - https://leetcode.com/problems/two-sum/description

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}

        for i in range(len(nums)):
            hashmap[nums[i]] = i
        
        indices = [0] * 2
        for i in range(len(nums)):
            if (target - nums[i]) in hashmap and hashmap[target-nums[i]] != i:
                indices[0] = i
                indices[1] = hashmap[target - nums[i]]
                return indices


        return []