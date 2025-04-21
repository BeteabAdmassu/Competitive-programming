# Problem: Design Circular Queue - https://leetcode.com/problems/design-circular-queue/

class MyCircularQueue:

    def __init__(self, k: int):
        self.k = k
        self.queue = [-1]*k
        self.start = 0
        self.rear = -1
        self.count = 0
        

    def enQueue(self, value: int) -> bool:
        valid = True
        if self.count == self.k:
            return False
        self.count = self.count+1 if self.count < self.k else self.k
        self.rear = (self.rear+1)%self.k
        self.queue[self.rear] = value
        return True
        

    def deQueue(self) -> bool:
        if self.count == 0:
            return False
        self.queue[self.start] = -1
        self.start = (self.start+1)%self.k
        self.count -= 1
        return True
        

    def Front(self) -> int:
        if self.count == 0:
            return -1
        return self.queue[self.start]
        

    def Rear(self) -> int:
        return self.queue[self.rear]
        

    def isEmpty(self) -> bool:
        return self.count == 0
        

    def isFull(self) -> bool:
        return self.count == self.k
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()