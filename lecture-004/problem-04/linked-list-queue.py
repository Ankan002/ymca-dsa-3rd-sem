"""
    ? Problem Statement: Q4 of Lecture 4
    
    ! Time Complexity:
        ! - Enqueue: O(1)
        ! - Dequeue: O(1)
        ! - IsEmpty: O(1)
        ! - Top: O(1)
        ! - Display: O(n)
"""

class Node:
    def __init__(self, val: int) -> None:
        self.val = val
        self.next: Node or None = None
        
class Queue:
    def __init__(self) -> None:
        self.front: Node or None = None
        self.rear: Node or None = None
        
    def enqueue(self, val: int) -> None:
        new_node = Node(val)
        
        if self.front == None:
            self.front = new_node
            self.rear = new_node
            
        self.rear.next = new_node
        self.rear = new_node
        
    def dequeue(self) -> int:
        if self.front == None: raise Exception("Queue Underflow!!")
        
        if self.rear == self.front:
            returning_num = self.front.val
            self.front = None
            self.rear = None
            return returning_num
        
        temp = self.front
        returning_num = temp.val
        self.front = self.front.next
        temp.next = None
        return returning_num
    
    def getFront(self) -> int:
        if self.front == None: raise Exception("Queue Underflow!!")
        
        return self.front.val
    
    def isEmpty(self) -> bool: return self.front == None
    
    def display(self) -> None:
        temp = self.front
        
        while temp != None:
            print(temp.val)
            temp = temp.next
            

queue = Queue()

print(queue.isEmpty())

queue.enqueue(12)
queue.enqueue(13)
queue.enqueue(11)
queue.enqueue(44)

print("The Queue is: ")
queue.display()

print(queue.isEmpty())
print(queue.getFront())

print(f"Dequeued Element: {queue.dequeue()}")