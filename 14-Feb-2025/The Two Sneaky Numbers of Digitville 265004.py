# Problem: The Two Sneaky Numbers of Digitville - https://leetcode.com/problems/the-two-sneaky-numbers-of-digitville/description

class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        hashmap = Counter(nums)
        output = []
        for value in hashmap:
            if hashmap[value] > 1: 
                output.append(value)

        return output