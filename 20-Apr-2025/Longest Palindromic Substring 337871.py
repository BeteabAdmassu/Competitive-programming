# Problem: Longest Palindromic Substring - https://leetcode.com/problems/longest-palindromic-substring/description/

class Solution:
    def longestPalindrome(self, s: str) -> str:
        result = ""
        resultLength = 0

        for i in range(len(s)):
            left = right = i
            
            while left >= 0 and right < len(s) and s[left] == s[right]:
                currentLength = right - left + 1

                if currentLength > resultLength:
                    result = s[left: right + 1]
                    resultLength = currentLength
                left -= 1
                right += 1

            left,right = i,i+1

            while left >= 0 and right < len(s) and s[left] == s[right]:
                currentLength = right - left + 1
                
                if currentLength > resultLength:
                    result = s[left: right + 1]
                    resultLength = currentLength
                left -= 1
                right += 1
        
        return result