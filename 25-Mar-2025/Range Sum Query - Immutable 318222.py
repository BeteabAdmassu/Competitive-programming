# Problem: Range Sum Query - Immutable - https://leetcode.com/problems/range-sum-query-immutable/

class NumArray:

    def __init__(self, nums: List[int]):
        self.arr = [0] * len(nums)
        sum = 0
        for i in range(len(nums)):
            sum += nums[i]
            self.arr[i] += sum
    def sumRange(self, left: int, right: int) -> int:
        
        if left - 1 is not -1:
            return self.arr[right] - self.arr[left - 1]
        else:
            return self.arr[right]
       
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)