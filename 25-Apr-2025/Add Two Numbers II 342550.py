# Problem: Add Two Numbers II - https://leetcode.com/problems/add-two-numbers-ii/description/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        l1_temp = l1
        l2_temp = l2


        s1 = ""
        s2 = ""

        while l1_temp:
            s1 += str(l1_temp.val)
            l1_temp = l1_temp.next
        while l2_temp:
            s2 += str(l2_temp.val)
            l2_temp = l2_temp.next

        
        summation = int(s1) + int(s2)

        outputNode = ListNode()

        current = outputNode


        str_summation = str(summation)

        for val in str_summation:
            node = ListNode(int(val))
            current.next = node
            current = current.next

        return outputNode.next

