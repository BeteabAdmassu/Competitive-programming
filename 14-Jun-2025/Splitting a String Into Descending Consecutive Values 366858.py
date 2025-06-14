# Problem: Splitting a String Into Descending Consecutive Values - https://leetcode.com/problems/splitting-a-string-into-descending-consecutive-values/

class Solution:
    def splitString(self, s: str) -> bool:
        n = len(s)
        
        def dfs(index, prev_value, count):
            if index == n:
                return count >= 2
            for j in range(index + 1, n + 1):
                current_value = int(s[index:j])
                if count == 0:
                    if dfs(j, current_value, count + 1):
                        return True
                else:
                    if current_value == prev_value - 1:
                        if dfs(j, current_value, count + 1):
                            return True
                    elif current_value > prev_value - 1:
                        break
            return False
        
        return dfs(0, 0, 0)