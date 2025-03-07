# Problem: Reduction Operations to Make the Array Elements Equal - LeetCode - https://leetcode.com/problems/reduction-operations-to-make-the-array-elements-equal/description/

class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        nums.sort(reverse= True)

        count = 0
        j = 0
        for i in range(1, len(nums)):
            if nums[i] != nums [i-1]:
                count += 1 + j
            j += 1
        return count
