# Problem: Relative Sort Array
(Easy) - https://leetcode.com/problems/relative-sort-array/

class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        arr1ToArr2 = {num: idx for idx, num in enumerate(arr2)}

        def customComparator(item):
            if item in arr1ToArr2:
                return (0, arr1ToArr2[item])
            else:
                return (1, item)
        
        arr1.sort(key=customComparator)
        
        return arr1