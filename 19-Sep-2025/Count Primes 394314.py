# Problem: Count Primes - https://leetcode.com/problems/count-primes/

class Solution:
    def countPrimes(self, n: int) -> int:
        prime = [True for _ in range(n)]
        if n > 2:
            prime[0] = prime[1] = False
        else:
            return 0


        i = 2
        while i <= n-1:
            if prime[i]:
                j = 2 * i
                while j <= n-1:
                    prime[j] = False
                    j += i
            i += 1
        count = sum([1 for x in prime if x == True])

        return count