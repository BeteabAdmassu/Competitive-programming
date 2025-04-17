# Problem: Palindrome Linked List - https://leetcode.com/problems/palindrome-linked-list/

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        current = head
        store = []

        while current:
            store.append(current.val)
            current = current.next

        l , r = 0, len(store)- 1

        while l <= r:
            if store[l] != store[r]:
                return False
            l += 1
            r -= 1

        return True
        
        