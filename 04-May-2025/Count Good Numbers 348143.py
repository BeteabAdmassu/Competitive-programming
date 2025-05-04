# Problem: Count Good Numbers - https://leetcode.com/problems/count-good-numbers/

class Solution:
    def countGoodNumbers(self, n: int) -> int:
        m = 10**9 + 7
        even = (n+1) // 2
        prime = (n) // 2
        output = 0
        
        output = (pow(5, even, m) * pow(4, prime, m)) % m
        
        return output
        
        