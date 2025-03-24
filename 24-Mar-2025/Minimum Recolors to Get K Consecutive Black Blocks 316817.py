# Problem: Minimum Recolors to Get K Consecutive Black Blocks - https://leetcode.com/problems/minimum-recolors-to-get-k-consecutive-black-blocks/

class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        left, right = 0 , 0
        op = 0
        minOp = float('inf')

        while right < len(blocks):
            if right - left < k:
                if blocks[right] == 'W':
                    op += 1
                if right - left == k - 1:
                    minOp = min(minOp,op)   
                right += 1

            else:
                minOp = min(minOp,op)
                if blocks[left] == 'W':
                    op -= 1
                left += 1
        return minOp
                



        