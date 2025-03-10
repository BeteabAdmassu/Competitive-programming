# Problem: Remove Duplicates from Sorted Array - https://leetcode.com/problems/remove-duplicates-from-sorted-array/

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        hashMap = set()
        index = 0 

        for num in nums:
            if num not in hashMap:
                hashMap.add(num)
                nums[index] = num
                index += 1
        return index
        
        
            


        
        
        