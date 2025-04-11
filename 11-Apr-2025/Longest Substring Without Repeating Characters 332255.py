# Problem: Longest Substring Without Repeating Characters - https://leetcode.com/problems/longest-substring-without-repeating-characters/description/

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        longest_substring = 0 

        left, right = 0, 0
        char_set = set()
      

        while right < len(s):

            if s[right] not in char_set:
                char_set.add(s[right])
                right += 1
                longest_substring = max(longest_substring, right - left)

            else:
                char_set.discard(s[left])
                left += 1
    
        return longest_substring

