# Problem: Roman to Integer - https://leetcode.com/problems/roman-to-integer/?envType=problem-list-v2&envId=string

class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        previous = ""
        output = 0

        for i in s[::-1]:
            if previous == "":
                previous = i
                output += roman[i]
            elif roman[i] < roman[previous]:
                previous = i
                output -= roman[i]
            else:
                previous = i
                output += roman[i]
        return output
            
        