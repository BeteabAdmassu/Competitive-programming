# Problem: 1561. Maximum Number of Coins You Can Get - https://leetcode.com/problems/maximum-number-of-coins-you-can-get/description/

class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        _max = 0
        n = len(piles)
        piles.sort()
        for i in range(n // 3, n, 2):
            _max += piles[i ]

        return _max


        # [[1,4,5 ], [ 2,6,7] , [ 3,8,9]]