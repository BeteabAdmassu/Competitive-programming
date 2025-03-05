# Problem: The Maximum Number - https://leetcode.com/problems/third-maximum-number/description/

class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        setNums = set(nums)
        distinct_val = 0
        _max = 0
        for num in range(3):
            if len(setNums) > 0:
                distinct_val = max(setNums)
                _max = max(_max,distinct_val)
                setNums.discard(distinct_val)
            else:
                return _max
            

        return distinct_val




        