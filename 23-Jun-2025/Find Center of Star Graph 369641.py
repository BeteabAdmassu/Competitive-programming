# Problem: Find Center of Star Graph - https://leetcode.com/problems/find-center-of-star-graph/

class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        nums = defaultdict(int)
        for u, v in edges:
            nums[u] += 1
            nums[v] += 1
            if nums[u] > 1:
                return u
            if nums[v] > 1:
                return v
        return -1