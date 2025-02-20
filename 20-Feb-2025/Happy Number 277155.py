# Problem: Happy Number - https://leetcode.com/problems/happy-number/description/

class Solution:
    def isHappy(self, n: int) -> bool:
        hashSet = set()

        while n != 1:
            if n in hashSet:
                return False
            hashSet.add(n)
            n = sum(int(num) ** 2 for num in str(n))
        return True