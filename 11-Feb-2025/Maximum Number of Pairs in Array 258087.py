# Problem: Maximum Number of Pairs in Array - https://leetcode.com/problems/maximum-number-of-pairs-in-array/description/

class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        hashmap = Counter(nums)
        pair = 0
        single = 0
        for num in hashmap:
            pair += hashmap[num] // 2
            single += hashmap[num] % 2
        return [pair, single]

        