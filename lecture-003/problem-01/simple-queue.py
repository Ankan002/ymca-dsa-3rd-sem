class SimpleQueue:
    def __init__(self) -> None:
        self.queue: list[int] = []
        self.front: int = -1
        self.rear: int  = -1
        
    def enqueue(self, num: int) -> None:
        self.queue.append(num)
        self.rear += 1
        
    def dequeue(self) -> int:
        if self.front == self.rear: raise Exception("Queue Underflow Exception!!")
        self.front += 1
        value = self.queue[self.front]
        self.queue[self.front] = None
        return value
        
    def display(self) -> None:
        if self.front == self.rear: raise Exception("Queue Underflow Exception!!")
        for i in range(self.front + 1, self.rear + 1):
            print(self.queue[i], end=" ")
            
        print()    
            
    def top(self) -> int:
        if self.front == self.rear: raise Exception("Queue Underflow Exception!!")
        return self.queue[self.front + 1]
    
simpleQueue = SimpleQueue()

simpleQueue.enqueue(13)
simpleQueue.enqueue(45)
simpleQueue.enqueue(89)

print(simpleQueue.dequeue())

simpleQueue.display()

print(simpleQueue.top())

print(simpleQueue.dequeue())
print(simpleQueue.dequeue())