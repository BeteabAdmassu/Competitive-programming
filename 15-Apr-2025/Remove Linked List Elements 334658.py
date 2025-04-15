# Problem: Remove Linked List Elements - https://leetcode.com/problems/remove-linked-list-elements/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:

        while head and head.val == val:
            temp = head
            head = head.next
            del temp

        currentNode = head
        prev = currentNode

        while currentNode:

            if currentNode.val == val:
                prev.next = currentNode.next
                temp = currentNode
                currentNode = currentNode.next
                del temp
            else:
                prev = currentNode
                currentNode = currentNode.next
        return head
        