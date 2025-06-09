# Problem: Additive Number - https://leetcode.com/problems/additive-number/

class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        n = len(num)
        if n < 3:
            return False
        
        for i in range(1, n):
            for j in range(i+1, n):
                num1_str = num[:i]
                num2_str = num[i:j]
                
                if (len(num1_str) > 1 and num1_str[0] == '0') or (len(num2_str) > 1 and num2_str[0] == '0'):
                    continue
                
                num1 = int(num1_str)
                num2 = int(num2_str)
                
                k = j
                valid = True
                remaining = num[k:]
                while remaining:
                    next_num = num1 + num2
                    next_str = str(next_num)
                    if not remaining.startswith(next_str):
                        valid = False
                        break
                    k += len(next_str)
                    remaining = num[k:]
                    num1, num2 = num2, next_num
                
                if valid and k == n and (n - j) >= 1:
                    return True
        return False