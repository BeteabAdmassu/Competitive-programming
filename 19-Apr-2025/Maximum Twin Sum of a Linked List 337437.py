# Problem: Maximum Twin Sum of a Linked List - https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list/description/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        result = 0

        stack = []
        current_node = head
        while current_node:
            stack.append(current_node.val)
            current_node = current_node.next

        stack.reverse()
        current_node = head

        for i in range(len(stack) // 2):
            result = max(result, stack[i] + current_node.val)
            current_node = current_node.next

        return result