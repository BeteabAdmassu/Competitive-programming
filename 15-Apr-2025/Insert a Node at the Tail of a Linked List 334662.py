# Problem: Insert a Node at the Tail of a Linked List - https://www.hackerrank.com/challenges/insert-a-node-at-the-tail-of-a-linked-list/problem

def insertNodeAtTail(head, data):
    node = SinglyLinkedListNode(data)
    
    if head is None:
        return node
    
    current = head
    while current.next:
        current = current.next
    current.next = node
    
    return head