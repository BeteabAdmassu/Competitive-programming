# Problem: Container With Most Water - https://leetcode.com/problems/container-with-most-water/

class Solution:
    def maxArea(self, height: List[int]) -> int:
        left , right = 0 , len(height) - 1
        maxVal = 0

        while left < right:
            maxVal = max(min(height[left], height[right]) * (right-left), maxVal)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return maxVal