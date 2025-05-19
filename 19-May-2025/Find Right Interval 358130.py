# Problem: Find Right Interval - https://leetcode.com/problems/find-right-interval/

class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        start_indices = [(interval[0], i) for i, interval in enumerate(intervals)]
        start_indices.sort()
    
        starts = [start for start, index in start_indices]
        indices = [index for start, index in start_indices]
    
        res = []
        for interval in intervals:
            end = interval[1]
            left, right = 0, len(starts) - 1
            found = -1
            while left <= right:
                mid = left + (right - left) // 2
                if starts[mid] >= end:
                    found = indices[mid]
                    right = mid - 1
                else:
                    left = mid + 1
            res.append(found)
        return res
        