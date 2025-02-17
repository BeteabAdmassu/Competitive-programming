# Problem: Majority Element II - https://leetcode.com/problems/majority-element-ii/?envType=daily-question&envId=2023-10-05

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        numshash = Counter(nums)
        output = []
        
        for num in numshash:
            if  numshash[num] > len(nums) / 3:
                output.append(num)
        return output
        