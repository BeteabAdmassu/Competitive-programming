# Problem: Number of Subarrays With LCM Equal to K - https://leetcode.com/problems/number-of-subarrays-with-lcm-equal-to-k/description/?envType=problem-list-v2&envId=number-theory

class Solution:
    def subarrayLCM(self, nums: List[int], k: int) -> int:
        count=0
        n=len(nums)
        def gcd(a,b):
            while b:
                a,b=b,a%b
            return a 
        def lcm(a,b):
            if a==0 or b==0:
                return 0
            return (a*b)//gcd(a,b)
        n=len(nums)
        count 


        for i in range(n):
            current_lcm=1
            for j in range(i,n):
                if k%nums[j]!=0:
                   break 

                current_lcm=lcm(current_lcm,nums[j])
                if current_lcm==k:
                    count+=1
                elif current_lcm>k:
                    break 
        return count 
        def gcd(a,b):
            lcm=a*b/(math.gcd(a,b))
            return lcm 
    