# Problem: Majority Element II (Optional) - https://leetcode.com/problems/majority-element-ii/

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        numshash = Counter(nums)

        output = []

        for num in numshash:
            if  numshash[num] > len(nums) / 3:
                output.append(num)
        return output
        