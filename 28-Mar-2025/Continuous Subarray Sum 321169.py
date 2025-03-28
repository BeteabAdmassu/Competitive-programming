# Problem: Continuous Subarray Sum - https://leetcode.com/problems/continuous-subarray-sum/

def checkSubarraySum(nums, k):
    n = len(nums)
    for i in range(n):
        current_sum = 0
        for j in range(i + 1, n):
            current_sum += nums[j]
            if current_sum % k == 0:
                return True
    return False