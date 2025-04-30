# Problem: Power of Four - https://leetcode.com/problems/power-of-four/

class Solution(object):
    def isPowerOfFour(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n == 1:
            return True
        elif n <= 0 or n % 4 != 0:
            return False
        else: 
            return self.isPowerOfFour( n // 4)