# Problem: Smallest Value of the Rearranged Number - https://leetcode.com/problems/smallest-value-of-the-rearranged-number/description/

class Solution:
    def smallestNumber(self, num: int) -> int:
        if num > 0:
            s = str(num)
            sl = [i for i in s]
            sls = sorted(sl , key =  lambda x: int(x))

            flag = False
            prev = 0
            for i in range(len(sls)):
                if sls[i] == "0" :
                    prev = min(prev,i)
                    flag = True
                if flag and sls[i] != "0":
                    sls[i], sls[prev] = sls[prev],sls[i]
                    break
            return int(''.join(sls))
        elif num < 0:
            s = str(num)
            sl = [i for i in s]
            sl = sl[1::]
      
            sls = sorted(sl , key =  lambda x: int(x), reverse=True)
            return -int("".join(sls))
        else:
            return 0
           
                    

        