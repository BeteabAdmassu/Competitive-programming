# Problem: Sort Colors - https://leetcode.com/problems/sort-colors/

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        hashnum = Counter(nums)
        print(hashnum)
        ptr = 0
        for i in range(3):
            while hashnum[i] != 0:
                nums[ptr] = i
                ptr += 1
                hashnum[i] -= 1

        return hashnum


        