# Problem: Longest Substring Without Repeating Characters - https://leetcode.com/problems/longest-substring-without-repeating-characters/

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        longest_substring = 0 
        counter = 0 

        left, right = 0, 0
        char_set = set()
      

        while right < len(s):

            if s[right] not in char_set:
                char_set.add(s[right])
                counter += 1
                longest_substring = max(longest_substring, counter)
                right += 1

            else:
                char_set.clear()
                right = left
                left += 1
                counter = 0
    
        return longest_substring



        