class Node:
    def __init__(self, val: int) -> None:
        self.val = val
        self.next: Node or None = None
        
class LinkedList:
    def __init__(self) -> None:
        self.head = None
            
    def addFront(self, val: int) -> None:
        new_node = Node(val)
        
        if self.head == None:
            self.head = new_node
            return
        
        new_node.next = self.head
        self.head = new_node
        
    def searchList(self, val: int) -> bool:
        temp = self.head
        
        while temp != None:
            if temp.val == val: return True
            temp = temp.next
            
        return False
    
ll = LinkedList()

ll.addFront(2)
ll.addFront(12)
ll.addFront(22)
ll.addFront(72)
ll.addFront(23)
ll.addFront(27)
ll.addFront(29)

print(ll.searchList(27))
print(ll.searchList(21))
        