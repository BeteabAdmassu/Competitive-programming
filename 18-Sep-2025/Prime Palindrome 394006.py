# Problem: Prime Palindrome - https://leetcode.com/problems/prime-palindrome/description/?envType=problem-list-v2&envId=number-theory

class Solution:
    def primePalindrome(self, n: int) -> int:
        if n <= 2:
            return 2
        if 8 <= n <= 11:
            return 11
        
        def is_prime(x):
            if x < 2:
                return False
            if x % 2 == 0:
                return x == 2
            r = int(x ** 0.5)
            for i in range(3, r + 1, 2):
                if x % i == 0:
                    return False
            return True
        
        def create_palindrome(base, odd_length):
            s = str(base)
            if odd_length:
                return int(s + s[-2::-1])
            else:
                return int(s + s[::-1])
        
        length = len(str(n))
        
        while True:
            half_len = (length + 1) // 2
            start = 10 ** (half_len - 1)
            end = 10 ** half_len
            
            for base in range(start, end):
                pal = create_palindrome(base, odd_length=True)
                if pal >= n and is_prime(pal):
                    return pal
            length += 1