# Problem: Number of Boomerangs - https://leetcode.com/problems/number-of-boomerangs/description/

class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        n = len(points)
        result = 0
        for i in range(n):
            dist_map = {}
            for j in range(n):
                if i != j:
                    dx = points[i][0] - points[j][0]
                    dy = points[i][1] - points[j][1]
                    dist = dx * dx + dy * dy
                    dist_map[dist] = dist_map.get(dist, 0) + 1
            for count in dist_map.values():
                if count > 1:
                    result += count * (count - 1)
        return result