# Problem: Merge Intervals (Optional) - https://leetcode.com/problems/merge-intervals/

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []

        
        intervals.sort(key=lambda x: x[0])

        output = []
        prev = intervals[0]

        for interval in intervals[1:]:
            if interval[0] <= prev[1]:
               
                prev[1] = max(prev[1], interval[1])
            else:
               
                output.append(prev)
                prev = interval

    
        output.append(prev)

        return output

    