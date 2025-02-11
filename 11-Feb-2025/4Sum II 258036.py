# Problem: 4Sum II - https://leetcode.com/problems/4sum-ii/

class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        
        firstHalf = defaultdict(int) 
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                firstHalf[nums1[i] + nums2[j]] += 1
                
        count = 0
        for i in range(len(nums3)):
            for j in range(len(nums4)):
                complement = -(nums3[i] + nums4[j])
                if complement in firstHalf:
                    count += firstHalf[complement]

        return count
                