"""
    ? Problem Statement: Q3 of Lecture 4
    
    ! Time Complexity:
        ! - Push: O(1)
        ! - Pop: O(1)
        ! - IsEmpty: O(1)
        ! - Top: O(1)
        ! - Display: O(n)
"""

class Node:
    def __init__(self, val: int) -> None:
        self.val = val
        self.next: Node or None = None
        
class Stack:
    def __init__(self) -> None:
        self.top: Node or None = None
        
    def push(self, val: int) -> None:
        new_node = Node(val)
        
        if self.top == None:
            self.top = new_node
            return
        
        new_node.next = self.top
        self.top = new_node
        
    def pop(self) -> int:
        if self.top == None: raise Exception("Stack Underflow!!!")
        
        if self.top.next == None:
            returning_num = self.top.val
            self.top = None
            return returning_num
        
        temp = self.top
        returning_num = temp.val
        self.top = self.top.next
        temp.next = None
        return returning_num
        
    def top(self) -> int:
        if self.top == None: raise Exception("Stack Underflow!!!")
        
        return self.top.val
    
    def isEmpty(self) -> bool: return self.top == None
    
    def display(self) -> None:
        temp = self.top
        
        while temp != None:
            print(temp.val)
            temp = temp.next
            
stack = Stack()

stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
stack.push(5)
stack.push(6)
stack.push(7)
stack.push(8)
stack.push(9)
stack.push(10)

print("My stack is:")
stack.display()

print(f"Popped out element is: {stack.pop()}")