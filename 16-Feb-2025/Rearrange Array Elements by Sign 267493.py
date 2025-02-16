# Problem: Rearrange Array Elements by Sign - https://leetcode.com/problems/rearrange-array-elements-by-sign/description/

class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        negative = []
        positive = []
        output = []

    

        for num in nums:
            if num < 0:
                negative.append(num)
            else:
                positive.append(num)

        print(negative)
        print(positive)

        
        for a,b in zip(positive,negative):
            output.append(a)
            output.append(b)

        return output


        # for i in range (0,len(nums)//2,2):
        #     temp = nums[i]
        #     nums[i] = nums[(len(nums) - 1) - i]
        #     nums[(len(nums) - 1) - i] = temp
        
        # return nums


        