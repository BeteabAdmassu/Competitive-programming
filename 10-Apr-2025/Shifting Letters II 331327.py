# Problem: Shifting Letters II - https://leetcode.com/problems/shifting-letters-ii/description/

class Solution(object):
    def shiftingLetters(self, s, shifts):
        length = len(s)
        changes = [0] * length 

        for start, end, direction in shifts:
            if direction == 1:  
                changes[start] += 1
                if end + 1 < length:
                    changes[end + 1] -= 1
            else: 
                changes[start] -= 1
                if end + 1 < length:
                    changes[end + 1] += 1

        shift = 0
        result = list(s)

        for i in range(length):
            shift = (shift + changes[i]) % 26
            if shift < 0:
                shift += 26

            new_letter = chr((ord(s[i]) - ord('a') + shift) % 26 + ord('a'))
            result[i] = new_letter

        return "".join(result)