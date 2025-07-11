# Problem: Remove Stones to Minimize the Total - https://leetcode.com/problems/remove-stones-to-minimize-the-total/

class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        max_heap = [-p for p in piles]
        heapq.heapify(max_heap)

        for _ in range(k):
            max_pile = -heapq.heappop(max_heap)
            new_pile = max_pile - (max_pile // 2)
            heapq.heappush(max_heap, -new_pile)

        return -sum(max_heap)