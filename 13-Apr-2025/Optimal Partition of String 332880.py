# Problem: Optimal Partition of String - https://leetcode.com/problems/optimal-partition-of-string/

class Solution:
    def partitionString(self, s: str) -> int:
        count = 1 

        s_set = set()

        for char in s:
            if char in s_set:
                count += 1
                s_set = {char}
            else:
                s_set.add(char)
        return count
        