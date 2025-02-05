# Problem: Masking Personal Information - https://leetcode.com/problems/masking-personal-information/description/?envType=problem-list-v2&envId=string

class Solution:
    def maskPII(self, s: str) -> str:
        s = s.lower()

        arr = s.split("@")
        masked = ""
        if len(arr)> 1:
            return f"{arr[0][0]}*****{arr[0][-1]}@{arr[-1]}"

        num = []
        for char in s:
            if char.isnumeric():
                num.append(char)
        phone = "".join(num)

        if len(phone) == 10:
            return f"***-***-{phone[-4:]}"
        elif len(phone) == 11:
            return f"+*-***-***-{phone[-4:]}"
        elif len(phone) == 12:
            return f"+**-***-***-{phone[-4:]}"    
        elif len(phone) == 13:
            return f"+***-***-***-{phone[-4:]}"   

        
