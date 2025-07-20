# Problem: Largest Odd Number in String - https://leetcode.com/problems/largest-odd-number-in-string/

class Solution:
    def largestOddNumber(self, num: str) -> str:
        n = list(map(int, num))
        for i in range(len(n)-1, -1, -1):
            if n[i] % 2 != 0:
                return "".join(map(str, n[:i+1]))
        return ""
        