# Problem: Permutation in String - https://leetcode.com/problems/permutation-in-string/

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        sorted_s1 = "".join(sorted(s1)) 
        m, n = len(s1), len(s2)

        for i in range(n-m + 1 ): 
            print(i)
            if sorted_s1 == "".join(sorted(s2[i:i + m])): 
                return True

        return False

        


        
        