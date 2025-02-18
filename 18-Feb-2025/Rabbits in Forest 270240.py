# Problem: Rabbits in Forest - https://leetcode.com/problems/rabbits-in-forest/

class Solution:
    def numRabbits(self, answers: List[int]) -> int:

        count_map = Counter(answers)
        total_rabbits = 0
    
        for x, count in count_map.items():
            groups = ceil(count / (x + 1))
            total_rabbits += groups * (x + 1)
    
        return total_rabbits