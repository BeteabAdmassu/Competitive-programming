# Problem: Row With Maximum Ones - https://leetcode.com/problems/row-with-maximum-ones/

class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:

        _max = 0
        index = 0
        for i in range(len(mat)):
            hashmap = Counter(mat[i])

            if hashmap[1] > _max:
                _max = hashmap[1]
                index = i
        return [index,_max]
        