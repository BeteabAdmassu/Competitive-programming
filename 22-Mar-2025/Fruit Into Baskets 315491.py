# Problem: Fruit Into Baskets - https://leetcode.com/problems/fruit-into-baskets

class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        left = 0
        maximum = 0
        basket = {}
        
        for right in range(len(fruits)):
            fruit = fruits[right]
            
            if fruit not in basket:
                basket[fruit] = 0
            basket[fruit] += 1
            
            while len(basket) > 2:
                basket[fruits[left]] -= 1
                if basket[fruits[left]] == 0:
                    del basket[fruits[left]]
                left += 1
        
            maximum = max(maximum, right - left + 1)
        
        return maximum
