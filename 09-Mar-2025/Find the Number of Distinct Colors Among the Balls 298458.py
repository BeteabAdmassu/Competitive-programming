# Problem: Find the Number of Distinct Colors Among the Balls - https://leetcode.com/problems/find-the-number-of-distinct-colors-among-the-balls/description/


class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        color_map = {}  
        color_count = {}  
        result = [] 
        
        for x, y in queries:
            if x in color_map and color_map[x] == y:
                result.append(len(color_count))
                continue 
            
            if x in color_map:
                old_color = color_map[x]
                color_count[old_color] -= 1
                if color_count[old_color] == 0:
                    del color_count[old_color]
            
            color_map[x] = y
            color_count[y] = color_count.get(y, 0) + 1
            
            result.append(len(color_count))
        
        return result