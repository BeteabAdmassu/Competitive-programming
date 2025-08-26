# Problem: Hamming Distance - https://leetcode.com/problems/hamming-distance/

class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        max_len = max(x.bit_length(), y.bit_length())

        x_bin = format(x, f"0{max_len}b")
        y_bin = format(y, f"0{max_len}b")

        count = 0

        for i in range(max_len-1, -1, -1):
            if x_bin[i] != y_bin[i]:
                count += 1
        
        return count
        
