"""
    ? Problem Statement: Q5 of Lecture 4
    
    ! Time Complexity:
        ! - Insert at the front: O(1)
        ! - Insert at the end: O(1)
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
        
class CircularLinkedList:
    def __init__(self) -> None:
        self.head: Node or None = None
        self.tail: Node or None = None
        
    def addFront(self, val: int) -> None:
        newNode = Node(val)
        
        if self.head == None:
            self.head = newNode
            self.tail = newNode
            self.tail.next = self.head
            return
            
        newNode.next = self.head
        self.head = newNode
        self.tail.next = self.head
        
    def addEnd(self, val: int) -> None:
        newNode = Node(val)
        
        if self.head == None:
            self.head = newNode
            self.tail = newNode
            self.tail.next = self.head
            return
        
        self.tail.next = newNode
        self.tail = newNode
        self.tail.next = self.head
        
    def addPos(self, pos: int, val: int) -> None:
        if pos == 1:
            self.addFront(val)
            return
        
        if self.head == None: return
        
        currentPos = 1
        temp = self.head
        
        while currentPos != pos - 1 and temp.next != self.head:
            temp = temp.next
            currentPos += 1
            
        if currentPos != pos - 1: return
        
        newNode = Node(val)
        
        newNode.next = temp.next
        temp.next = newNode
        
        if temp == self.tail:
            self.tail = newNode
        
    def deleteFront(self) -> None:
        if self.head == None: return
        
        if self.head == self.tail:
            self.head = None
            self.tail = None
            return
            
        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.tail.next = self.head
        
    def deleteEnd(self) -> None:
        if self.head == None: return
        
        if self.head == self.tail:
            self.head = None
            self.tail = None
            return
        
        temp = self.head
        
        while temp.next.next != self.head:
            temp = temp.next
            
        self.tail.next = None
        self.tail = temp
        self.tail.next = self.head
        
    def deletePos(self, pos: int) -> None:
        if pos == 1:
            self.deleteFront()
            return
        
        if self.head == None: return
        
        currentPos = 1
        temp = self.head
        
        while currentPos != pos - 1 and temp.next.next != self.head:
            temp = temp.next
            currentPos += 1
            
        if currentPos != pos - 1: return
        
        if temp.next == self.tail:
            temp.next = self.tail.next
            self.tail.next = None
            self.tail = temp
            return
        
        nodeToBeDeleted = temp.next
        temp.next = nodeToBeDeleted.next
        nodeToBeDeleted.next = None
        
    def printList(self) -> None:
        temp = self.head
        
        if temp == None: return
        
        print(temp.val)
        temp = temp.next
        
        while temp != self.head:
            print(temp.val)
            temp = temp.next
            

# Driver Code
cll = CircularLinkedList()

cll.addPos(20, 22)
cll.addFront(12)
cll.addFront(22)
cll.addPos(3, 2)
cll.addEnd(60)
cll.addPos(2, 67)
cll.addPos(6, 120)
cll.addPos(1, 220)
cll.addEnd(160)

cll.deleteFront()
cll.deleteEnd()
cll.deletePos(6)
cll.deletePos(6)
cll.deletePos(1)
cll.deletePos(3)
cll.deletePos(2)

cll.printList()