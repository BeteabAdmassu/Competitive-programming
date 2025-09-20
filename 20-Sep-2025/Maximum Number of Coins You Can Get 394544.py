# Problem: Maximum Number of Coins You Can Get - https://leetcode.com/problems/maximum-number-of-coins-you-can-get/

class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        _max = 0
        n = len(piles)
        piles.sort()
        for i in range(n // 3, n, 2):
            _max += piles[i ]

        return _max


