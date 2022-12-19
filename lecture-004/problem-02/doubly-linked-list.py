"""
    ? Problem Statement: Q2 of Lecture 4
    
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
        self.prev: Node or None = None
        
class DoublyLinkedList:
    def __init__(self) -> None:
        self.head: Node or None = None
        
    def addFront(self, val: int) -> None:
        new_node = Node(val)
        
        if self.head == None:
            self.head = new_node
            return
        
        new_node.next = self.head
        self.head = new_node
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
        new_node.prev = temp
        
    def addPos(self, val: int, pos: int) -> None:
        if pos == 1:
            self.addFront(val)
            return
            
        if self.head == None: return
        
        temp = self.head
        currentPos = 1
        
        while temp.next != None and currentPos < pos - 1:
            temp = temp.next
            currentPos += 1
        
        if temp.next == None and currentPos != pos - 1: return
        
        new_node = Node(val)
        
        if temp.next == None and currentPos == pos - 1:
            temp.next = new_node
            new_node.prev = temp
            return
        
        new_node.next = temp.next
        new_node.prev = temp
        new_node.next.prev = new_node
        temp.next = new_node
        
    def deleteFront(self) -> None:
        if self.head == None: return
        
        if self.head.next == None:
            self.head = None
            return
        
        temp = self.head
        self.head = self.head.next
        
        temp.next = None
        self.head.prev = None
        
        
    def deleteEnd(self) -> None:
        if self.head == None: return
        
        if self.head.next == None:
            self.head = None
            return
        
        temp = self.head
        
        while temp.next != None:
            temp = temp.next
            
        temp.prev.next = None
        temp.prev = None
        
    def deleteAtPos(self, pos: int) -> None:
        if self.head == None: return
        
        if pos == 1:
            self.deleteFront()
            return
        
        currentPos = 1
        temp = self.head
        
        while temp != None and currentPos < pos - 1:
            temp = temp.next
            currentPos += 1
            
        if temp == None or temp.next == None: return
        
        if temp.next.next == None:
            temp.next.prev = None
            temp.next = None
            return
        
        nodeToBeDeleted = temp.next
        temp.next = nodeToBeDeleted.next
        nodeToBeDeleted.next.prev = temp
        nodeToBeDeleted.next = None
        nodeToBeDeleted.prev = None
            
        
    def printList(self) -> None:
        temp = self.head
        
        while temp != None:
            print(temp.val)
            temp = temp.next
            
    
dll = DoublyLinkedList()

dll.addFront(40)
dll.addEnd(9)
dll.addPos(29, 1)
dll.addPos(45, 4)
dll.addPos(12, 3)
dll.addPos(100, 20)

dll.deleteFront()
dll.deleteEnd()
dll.deleteAtPos(3)

dll.printList()