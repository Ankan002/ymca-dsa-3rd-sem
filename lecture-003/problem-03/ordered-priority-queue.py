"""
    ? Problem Statement: Q3(A) of lecture 3.
    
    ! Time Compilexity:
        !- enqueue: O(n)
        !- dequeue: O(1)
        !- isEmpty: O(1)
        !- top: O(1)
        !- display: O(n)
"""

class OrderedPriorityQueue:
    def __init__(self) -> None:
        self.queue: list[int] = []
        
    def enqueue(self, num: int) -> None:
        posToBeInserted = -1
        
        for i in range(len(self.queue)):
            if self.queue[i] >= num:
                posToBeInserted = i
                break
            
        if posToBeInserted == -1:
            self.queue.append(num)
            return
        
        self.queue.append(0)
        
        for i in range(len(self.queue) - 1, posToBeInserted, -1):
            self.queue[i] = self.queue[i-1]
            
        self.queue[posToBeInserted] = num
        
    def dequeue(self) -> int:
        if len(self.queue) == 0: raise Exception("Queue Underflow Exception!!")
        return self.queue.pop(0)
    
    def isEmpty(self) -> bool: return len(self.queue) == 0
    
    def top(self) -> int:
        if len(self.queue) == 0: raise Exception("Queue Underflow Exception!!")
        return self.queue[0]
    
    def display(self) -> None:
        for num in self.queue:
            print(num)
    
    
priority_queue = OrderedPriorityQueue()

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
