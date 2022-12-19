"""
    ? Problem Statement: Q1 of Lecture 4
    
    ! Time Complexity:
        ! - Insert at the front: O(1)
        ! - Insert at the end: O(n)
        ! - Insert at a position: O(n)
        ! - Delete from the front: O(1)
        ! - Delete from the end: O(n)
        ! - Delete from a position: O(n)
        ! - Print LinkedList: O(n)
"""

class Node:
    def __init__(self, val: int) -> None:
        self.val = val
        self.next: Node or None = None


class LinkedList:
    def __init__(self) -> None:
        self.head = None


    def printlist(self):
        temp = self.head
        while (temp):
            print(temp)
            temp = temp.next
            
    def addFront(self, val: int) -> None:
        new_node = Node(val)
        
        if self.head == None:
            self.head = new_node
            return
        
        new_node.next = self.head
        self.head = new_node
        
    def addEnd(self, val: int) -> None:
        new_node = Node(val)
        
        if self.head == None:
            self.head = new_node
            return
        
        temp = self.head
        
        while temp.next != None:
            temp = temp.next
            
        temp.next = new_node
        
    def addAtPos(self, val: int, pos: int) -> None:
        if pos == 1:
            self.addFront(val)
            return
            
        new_node = Node(val)
            
        current_pos = 1
        temp = self.head
        
        while current_pos < pos - 1 and temp.next != None:
            temp = temp.next
            current_pos += 1
            
        next = temp.next
        new_node.next = next
        temp.next = new_node
        
    def deleteFront(self) -> None:
        if self.head == None: return
        
        if self.head.next == None:
            self.head = None
            return
        
        temp = self.head
        self.head = self.head.next
        temp.next = None
        
    def deleteEnd(self) -> None:
        if self.head == None: return
        
        if self.head.next == None:
            self.heade = None
            return
        
        temp = self.head
        
        while temp.next.next != None:
            temp = temp.next
            
        temp.next = None
        
    def deletePos(self, pos: int) -> None:
        if self.head == None: return
        
        if pos == 1:
            self.deleteFront()
            return
        
        currentPos = 1
        temp = self.head
        prev = self.head
        
        while currentPos < pos and temp != None:
            prev = temp
            temp = temp.next
            currentPos += 1
            
        if temp == None == None: return
        
        prev.next = temp.next
        temp.next = None
        
        
    def printList(self):
        temp = self.head
        
        while temp != None:
            print(temp.val)
            temp = temp.next
            

ll = LinkedList()

ll.addFront(2)  
ll.addFront(3)  
ll.addFront(4)
ll.addEnd(10)
ll.addAtPos(11, 1)
ll.addAtPos(12, 6)
ll.addAtPos(17, 2)
# ll.deleteFront()
# ll.deleteEnd()
# ll.deletePos(2)

ll.printList()
        
    
