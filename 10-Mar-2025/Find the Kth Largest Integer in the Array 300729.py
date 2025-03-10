# Problem: Find the Kth Largest Integer in the Array - https://leetcode.com/problems/find-the-kth-largest-integer-in-the-array/

class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        temp = sorted(nums,key = lambda x:int(x))
   

        return temp[len(nums)-k]

            
        