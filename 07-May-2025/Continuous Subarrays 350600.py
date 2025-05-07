# Problem: Continuous Subarrays - https://leetcode.com/problems/continuous-subarrays/

class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        left, right = 0, 0
        min_queue = deque()
        max_queue = deque()
        result = 0
        while right < len(nums):
            while max_queue and max_queue[-1] < nums[right]:
                max_queue.pop()
            max_queue.append(nums[right])

            while min_queue and min_queue[-1] > nums[right]:
                min_queue.pop()
            min_queue.append(nums[right])

            while max_queue[0] - min_queue[0] > 2:
                if nums[left] == max_queue[0]:
                    max_queue.popleft()
                if nums[left] == min_queue[0]:
                    min_queue.popleft()
                left += 1
            result += right - left + 1
            right += 1

        return result
        