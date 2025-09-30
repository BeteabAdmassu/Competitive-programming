# Problem: Number of Matching Subsequences - https://leetcode.com/problems/number-of-matching-subsequences/

class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        result = 0
        visited_sub = {}
        for word in words:
            i = 0
            j = 0
            if word in visited_sub:
                if visited_sub[word]:
                    result += 1
                continue
            while i < len(word) and j < len(s):
                if word[i] == s[j]:
                    i += 1
                    j += 1
                else:
                    j += 1
            
            if i == len(word):
                visited_sub[word] = True
                result += 1
            else:
                visited_sub[word] = False
                
        return result