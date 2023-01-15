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
        
    def searchList(self, val: int) -> bool:
        if self.head == None: return False
        
        if self.head.val == val: return True
        
        temp = self.head.next
        
        while temp != self.head:
            if temp.val == val: return True
            
            temp = temp.next
            
        return False
    
ll = CircularLinkedList()

ll.addFront(2)
ll.addFront(12)
ll.addFront(22)
ll.addFront(72)
ll.addFront(23)
ll.addFront(27)
ll.addFront(29)

print(ll.searchList(27))
print(ll.searchList(21))