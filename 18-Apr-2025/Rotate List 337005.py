# Problem: Rotate List - https://leetcode.com/problems/rotate-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        length = 0
        current = head
        while current:
            length += 1
            current = current.next
            

        if length == 0:
            return head
            

        k = k % length
        if k == 0:
            return head
            
        slow = fast = head
        
        for _ in range(k):
            fast = fast.next
            
        while fast.next:
            fast = fast.next
            slow = slow.next
            
        fast.next = head
        head = slow.next
        slow.next = None
        
        return head
        