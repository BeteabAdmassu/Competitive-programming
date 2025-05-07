# Problem: Score of Parentheses - https://leetcode.com/problems/score-of-parentheses/

class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = []
        result = 0
        for char in s:
            if char == '(':
                stack.append(result)
                result = 0
            else:
                 result = stack.pop() + max(result * 2 , 1)

        return result
        