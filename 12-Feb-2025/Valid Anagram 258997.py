# Problem: Valid Anagram - https://leetcode.com/problems/valid-anagram/description/

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
       sorted_s = sorted(s)
       sorted_t = sorted(t)
       return sorted_s == sorted_t
