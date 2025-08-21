# Problem: Number Complement - https://leetcode.com/problems/number-complement/

class Solution:
    def findComplement(self, num: int) -> int:
        binary = []
	
        while (num != 0):
            binary.append(num % 2)
            num = num // 2

        binary.reverse()

        for i in range(len(binary)):
            if (binary[i] == 0):
                binary[i] = 1
            else:
                binary[i] = 0

        two = 1
        for i in range(len(binary) - 1, -1, -1):
            num = num + binary[i] * two
            two = two * 2

        return num
