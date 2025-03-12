# Problem: Valid Palindrome II - https://leetcode.com/problems/valid-palindrome-ii/description/

class Solution:
    def validPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1
        while left <= right:
            if s[left] != s[right]:
                skip_left = s[left + 1:right + 1]
                if skip_left == skip_left[::-1]:
                    return True
                skip_right = s[left:right]
                if skip_right == skip_right[::-1]:
                    return True
                return False
            left += 1
            right -= 1
        return True