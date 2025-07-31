# Problem: Best Time to Buy and Sell Stock - https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left, right = 0 , 0
        maxi = 0
        while right < len(prices) and left <= right:
            if left == right:
                right += 1
            elif prices[left] >= prices[right]:
                left = right
            elif prices[left] < prices[right]:
                diff = prices[right] - prices[left]
                right += 1
                if diff > maxi:
                    maxi = diff
        return maxi
            

       


        