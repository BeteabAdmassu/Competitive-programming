# Problem: Split Linked list in parts - https://leetcode.com/problems/split-linked-list-in-parts/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        length = 0
        current = head
        result = []

        while current is not None:
            length += 1
            current = current.next
        
        parts = length // k
        extra_part = length % k

        current = head

        for i in range(k):
            result_head = current
            if i < extra_part:
                result_size = parts + 1
            else:
                result_size = parts
            for j in range(result_size - 1):
                if current:
                    current = current.next
            if current:
                dummy = current.next
                current.next = None
                current = dummy
            result.append(result_head)
        return result
        