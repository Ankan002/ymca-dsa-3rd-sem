"""
    ? Problem Statement: Q2 of Lecture 3
    
    ! Time Complexity:
        ! - Enqueue: O(1)
        ! - Dequeue: O(1)
        ! - IsEmpty: O(1)
        ! - IsFull: O(1)
        ! - Front: O(1)
"""

class CircularQueue:
    def __init__(self, queueSize: int) -> None:
        self.queue = [None] * queueSize
        self.front = -1
        self.rear = -1
    
    def isFull(self) -> bool: return (self.front == 0 and self.rear == len(self.queue) - 1) or self.rear == self.front - 1
    
    def isEmpty(self) -> bool: return self.front == -1
    
    def enqueue(self, val: int) -> None:
        if self.isFull(): raise Exception("The queue is full")
        
        if self.rear == -1: self.front = 0
        
        self.rear += 1
        self.queue[(self.rear) % len(self.queue)] = val
        
    def dequeue(self) -> int:
        if self.isEmpty(): raise Exception("The queue is empty")
        
        poppedVal = self.queue[self.front]
        
        if self.front == self.rear:
            self.front = -1
            self.rear = -1
        else:
            self.front += 1
            
        return poppedVal
    
    def frontElement(self) -> int:
        if self.isEmpty(): raise Exception("The queue is empty")
        
        return self.queue[self.front]
    
# Driver Code
circularQueue = CircularQueue(3)

circularQueue.enqueue(2)
circularQueue.enqueue(4)
circularQueue.enqueue(5)

print(circularQueue.dequeue())
print(circularQueue.dequeue())

circularQueue.enqueue(12)
# circularQueue.enqueue(6)

print(circularQueue.frontElement())

print(circularQueue.isEmpty())
print(circularQueue.isFull())

# print(circularQueue.dequeue())