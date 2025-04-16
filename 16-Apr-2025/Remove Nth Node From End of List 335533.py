# Problem: Remove Nth Node From End of List - https://leetcode.com/problems/remove-nth-node-from-end-of-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        left = dummy
        temp = head
        counter = 0
        while counter < n:
            temp = temp.next
            counter += 1

        right = temp

        while right:
            right = right.next
            left = left.next

        left.next = left.next.next
        return dummy.next


        