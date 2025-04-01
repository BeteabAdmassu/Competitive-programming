# Problem: Sum of Square Numbers - https://leetcode.com/problems/sum-of-square-numbers/

class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        a, b = 0, int(math.sqrt(c))
    
        while a <= b:
            sum_of_squares = a * a + b * b
            if sum_of_squares == c:
                return True
            elif sum_of_squares < c:
                a += 1
            else:
                b -= 1
    
        return False