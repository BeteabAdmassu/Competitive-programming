# Problem: Check if All the Integers in a Range Are Covered - https://leetcode.com/problems/check-if-all-the-integers-in-a-range-are-covered/description/

class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        covered = True
        for i in range(left,right + 1):
            covered = False
            for rang in ranges:
                if rang[0] <= i <= rang[1]:
                    covered = True
                    break
            if not covered:
                return False
        return True




       