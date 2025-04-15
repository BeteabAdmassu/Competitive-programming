# Problem: Design Linked List - https://leetcode.com/problems/design-linked-list/

class MyLinkedList:

    def __init__(self):
        self.linked_list = []
        

    def get(self, index: int) -> int:
        if 0 <= index < len(self.linked_list):
            return self.linked_list[index]
        return -1
         

    def addAtHead(self, val: int) -> None:
        self.linked_list.insert(0, val)
        

    def addAtTail(self, val: int) -> None:
        self.linked_list.append(val)
        

    def addAtIndex(self, index: int, val: int) -> None:
        if 0 <= index <= len(self.linked_list):
            self.linked_list.insert(index, val) 

        

    def deleteAtIndex(self, index: int) -> None:
        if 0 <= index < len(self.linked_list):
            self.linked_list.pop(index) 
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)