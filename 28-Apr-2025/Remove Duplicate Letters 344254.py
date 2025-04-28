# Problem: Remove Duplicate Letters - https://leetcode.com/problems/remove-duplicate-letters/

class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        count = defaultdict(int)
        visited = defaultdict(bool)
        stack = []

        for char in s:
            count[char] += 1

        for char in s:
            count[char] -= 1

            if visited[char]:
                continue

            while stack and char < stack[-1] and count[stack[-1]] > 0:
                removed_char = stack.pop()
                visited[removed_char] = False

            stack.append(char)
            visited[char] = True

        return ''.join(stack)