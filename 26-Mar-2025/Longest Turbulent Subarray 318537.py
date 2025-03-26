# Problem: Longest Turbulent Subarray - https://leetcode.com/problems/longest-turbulent-subarray/

class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        if len(arr) < 2:
            return len(arr)


        left, right = 0 , 1
        greater = 0
        max_turbulent = 0
        turbulent = 0
        while right < len(arr) and left < right:
            if greater is 0:
                if arr[left] > arr[right]:
                    greater = False
                    turbulent = 2
                elif arr[left] < arr[right]:
                    greater = True
                    turbulent = 2
                else:
                    turbulent = 1
                left += 1
                right += 1
            
                max_turbulent = max(max_turbulent , turbulent)
                continue

            if arr[left] > arr[right]:
                if greater:
                    turbulent += 1
                    right += 1
                    left += 1
                    greater = False
                else:
                    max_turbulent = max(max_turbulent , turbulent)
                    turbulent = 0
                    greater = 0
            elif arr[left] < arr[right]:
               
                if greater:
                    max_turbulent = max(max_turbulent , turbulent)
                    turbulent = 0
                    greater = 0
                else:
                    turbulent += 1
                    greater = True
                    right += 1
                    left += 1
            else:
                
                right += 1
                left += 1
                turbulent = 0
                greater = 0
            
            max_turbulent = max(max_turbulent , turbulent)
        return max_turbulent




