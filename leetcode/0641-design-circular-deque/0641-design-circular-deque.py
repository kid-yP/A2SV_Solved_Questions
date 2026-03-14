class MyCircularDeque:

    def __init__(self, k: int):
        self.capacity = k
        self.deque = [0] * k
        self.front = 0
        self.rear = -1
        self.count = 0

    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False
            
        self.front = (self.front - 1 + self.capacity) % self.capacity
        self.deque[self.front] = value
        self.count += 1
        if self.count == 1:
            self.rear = self.front
        return True

    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False
        self.rear = (self.rear + 1) % self.capacity
        self.deque[self.rear] = value
        self.count += 1
        if self.count == 1:
            self.front = self.rear
        return True

    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False
        self.front = (self.front + 1) % self.capacity
        self.count -= 1
        return True

    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False
        self.rear = (self.rear - 1 + self.capacity) % self.capacity
        self.count -= 1
        return True

    def getFront(self) -> int:
        return -1 if self.isEmpty() else self.deque[self.front]

    def getRear(self) -> int:
        return -1 if self.isEmpty() else self.deque[self.rear]

    def isEmpty(self) -> bool:
        return self.count == 0

    def isFull(self) -> bool:
        return self.count == self.capacity