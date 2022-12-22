"""
    ? Problem Statement: Q3(B) of lecture 3.
    
    ! Time Compilexity:
        !- enqueue: O(1)
        !- dequeue: O(n)
        !- isEmpty: O(1)
        !- top: O(n)
        !- display: O(n)
"""

class UnorderedPriorityQueue:
    def __init__(self) -> None:
        self.queue: list[int] = []
        
    def enqueue(self, num: int) -> None:
        self.queue.append(num)
        
    def dequeue(self) -> int:
        if len(self.queue) == 0: raise Exception("Queue Underflow Exception!!")
        if len(self.queue) == 0: return self.queue.pop()
        
        lowestIndex = 0
        
        for i in range(1, len(self.queue)):
            if self.queue[lowestIndex] > self.queue[i]: lowestIndex = i
            
        poppedValue = self.queue[lowestIndex]
            
        for i in range(lowestIndex, len(self.queue) - 1):
            self.queue[i] = self.queue[i+1]
            
        self.queue.pop()
        
        return poppedValue
    
    def isEmpty(self) -> bool: return len(self.queue) == 0
    
    def top(self) -> int:
        if len(self.queue) == 0: raise Exception("Queue Underflow Exception!!")
        
        lowestIndex = 0
        
        for i in range(1, len(self.queue)):
            if self.queue[lowestIndex] > self.queue[i]: lowestIndex = i
            
        return self.queue[lowestIndex]
    
    def display(self) -> None:
        for num in self.queue:
            print(num)
            
            
priority_queue = UnorderedPriorityQueue()

priority_queue.enqueue(45)
priority_queue.enqueue(15)
priority_queue.enqueue(16)
priority_queue.enqueue(25)
priority_queue.enqueue(18)
priority_queue.enqueue(20)
priority_queue.enqueue(77)

print(priority_queue.top())

print(priority_queue.isEmpty())

print(priority_queue.dequeue())

print("The priority queue is: ")
priority_queue.display()