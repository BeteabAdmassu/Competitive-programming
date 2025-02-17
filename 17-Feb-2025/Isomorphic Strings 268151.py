# Problem: Isomorphic Strings - https://leetcode.com/problems/isomorphic-strings/

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:

        map1 = {i : j for i,j in zip(s,t)}
        map2 = {i : j for i,j in zip(t,s)}
        if len(map1) != len(map2):
            return False
        for i, j in zip(map1,map2):
            if map1[i] != j or map2[j] != i:
                return False
        return True