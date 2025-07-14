# Problem: Kth Smallest Element in a Sorted Matrix - https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/description/

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        combined = []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                combined.append(matrix[i][j])
        
        heapq.heapify(combined)
        sorted_combined = []
        for _ in range(k):
            smallest = heapq.heappop(combined)
            sorted_combined.append(smallest)
        return sorted_combined[-1]
        