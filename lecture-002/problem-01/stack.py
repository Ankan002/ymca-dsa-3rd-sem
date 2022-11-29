"""
    ? Problem Statement: Q1 of Lecture 02
    
    ! Time Complexity:
        ! - push: O(1)
        ! - pop: O(1)
        ! - top: O(1)
        ! - is empty: O(1)
        ! - print: O(n)
        
    ! Space Complexity: O(n)
"""

class Stack:
    def __init__(self) -> None:
        self.arr: list[int] = []
        
    def push(self, num: int) -> None :
        self.arr.append(num)
        
    def top(self) -> int:
        if len(self.arr) == 0: raise Exception("Stack Underflow!!")
        
        self.arr[len(self.arr) - 1]
        
    def pop(self) -> int:
        if len(self.arr) == 0: raise Exception("Stack Underflow!!")
        return self.arr.pop()
    
    def is_empty(self) -> bool:
        return len(self.arr) == 0
    
    def print_stack(self) -> None:
        for i in range(len(self.arr) - 1, -1, -1):
            print(self.arr[i])
    
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
stack.print_stack()

print(f"Popped out element is: {stack.pop()}")
        