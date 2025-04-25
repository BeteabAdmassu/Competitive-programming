# Problem: Valid Parentheses - https://leetcode.com/problems/valid-parentheses

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in s:
            if i is '(' or i is '[' or i is '{':
                stack.append(i)
            elif len(stack) > 0 and stack[len(stack) - 1] is '(' and i is ')':
                stack.pop(len(stack) - 1)
            elif len(stack) > 0 and stack[len(stack) - 1] is '[' and i is ']':
                stack.pop(len(stack) - 1)
            elif len(stack) > 0 and stack[len(stack) - 1] is '{' and i is '}':
                stack.pop(len(stack) - 1)
            else:
                return False
        if len(stack) is 0:
            return True
        
        return False