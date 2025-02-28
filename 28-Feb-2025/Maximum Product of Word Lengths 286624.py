# Problem: Maximum Product of Word Lengths - https://leetcode.com/problems/maximum-product-of-word-lengths/

class Solution:
    def maxProduct(self, words: List[str]) -> int:
        
        maximum_value = 0

        for i in range(len(words) - 1):

            for j in range(i + 1 , len(words)):
                if len(set(words[i]) & set(words[j])) == 0:
                    temp = len(words[i]) * len(words[j])
                    maximum_value = max(maximum_value,temp)

        return maximum_value