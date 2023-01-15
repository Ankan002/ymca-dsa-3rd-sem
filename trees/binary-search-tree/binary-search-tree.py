"""
    Problem Statement: Binary Search Tree
"""

class Node:
    def __init__(self, val: int) -> None:
        self.val = val
        self.left: None or Node = None
        self.right: None or Node = None


class BST:
    def insert(self, key: int, root: Node or None):
        node = Node(key)
        if (root == None):
            root = node
            return root
        prev = None
        temp = root
        while (temp != None):
            if (temp.val > key):
                prev = temp
                temp = temp.left
            elif (temp.val < key):
                prev = temp
                temp = temp.right
        if (prev.val > key):
            prev.left = node
        else:
            prev.right = node
        
        return root
            
    def __findMaxOnLeft(self, root: Node) -> int:
        currentNode = root.left
        
        while currentNode.right != None:
            currentNode = currentNode.right
            
        return currentNode.val

    def delete(self, key: int, root: Node or None) -> Node or None:
        if root == None: return None
        
        if root.val == key:
            if root.left == None and root.right == None:
                return None
            
            if root.right == None:
                return root.left
            
            if root.left == None:
                return root.right
            
            inorderPredecessor = self.__findMaxOnLeft(root)
            root.val = inorderPredecessor
            root.left = self.delete(inorderPredecessor, root.left)
            return root
        
        elif root.val < key: root.right = self.delete(key, root.right)
        
        else: root.left = self.delete(key, root.left)
        
        return root
    
    def inOrder(self, root: Node or None) -> None:
        if root == None: return
        
        self.inOrder(root.left)
        print(root.val, end=" ")
        self.inOrder(root.right)
        


tree = BST()
head = tree.insert(30, None)
tree.insert(50, head)
tree.insert(15, head)
tree.insert(20, head)
tree.insert(10, head)
tree.insert(40, head)
tree.insert(60, head)

tree.inOrder(head)

print()

tree.delete(50, head)
tree.delete(60, head)

tree.inOrder(head)

print()
