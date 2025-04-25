# Problem: Removing Stars From a String - https://leetcode.com/problems/removing-stars-from-a-string/description/

class Solution:
    def removeStars(self, s: str) -> str:

        stack = []

        for i in range(len(s)):
            if s[i] != '*':
                stack.append(s[i])
            else:
                stack.pop()
        return "".join(stack) 
        