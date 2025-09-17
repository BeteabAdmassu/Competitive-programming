# Problem: Smallest Value After Replacing With Sum of Prime Factors - https://leetcode.com/problems/smallest-value-after-replacing-with-sum-of-prime-factors/

class Solution:
    def smallestValue(self, n: int) -> int:
        def prime_factor_sum(x):
            total,num=0,x
            while num %2==0:
                total+=2
                num//=2
            factor = 3
            while factor * factor <=num:

                while num % factor == 0:
                    total +=factor 
                    num//=factor 
                factor +=2
            if num >1:
                total+=num 
            return total 
        while True:
            s=prime_factor_sum(n)
            if s==n:
                return n 
            n=s 