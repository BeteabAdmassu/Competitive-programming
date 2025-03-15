# Problem: Three sum - https://leetcode.com/problems/3sum/

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        answer = []

        for i , value in enumerate(nums):
            if i > 0 and value == nums[i - 1]:
                continue
            
            left , right = i + 1 , len(nums) - 1

            while left < right:
                threeSum = value + nums[left] + nums[right]

                if threeSum > 0:
                    right -= 1
                elif threeSum < 0:
                    left += 1
                else:
                    answer.append([ value, nums[left], nums[right]])
                    left += 1
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1
        return answer