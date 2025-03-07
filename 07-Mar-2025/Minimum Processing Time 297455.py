# Problem: Minimum Processing Time - https://leetcode.com/problems/minimum-processing-time/

class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
    
        processorTime.sort()
  
        tasks.sort(reverse=True)
    
        max_time = 0
  
        for i in range(len(processorTime)):
    
            cur = processorTime[i] + max(tasks[i * 4:i * 4 + 4])
            if cur > max_time:
                max_time = cur
    
        return max_time
        