class TreeNode:
    def __init__(self, val) -> None:
        self.val = val
        self.left: None or TreeNode = None
        self.right: None or TreeNode = None
        
class BST:
    def __init__(self):
        self.root: TreeNode or None = None
        
    def getRoot(self):
        return self.root
        
    def insert(self, key: int):
        node = TreeNode(key)
        if (self.root == None):
            self.root = node
            return
        prev = None
        temp = self.root
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
            
    def inOrder(self, root: TreeNode or None) -> None:
        if root == None: return
        
        self.inOrder(root.left)
        print(root.val, end=" ")
        self.inOrder(root.right)
        
    def preOrder(self, root: TreeNode or None) -> None:
        if root == None: return
        
        print(root.val, end=" ")
        self.preOrder(root.left)
        self.preOrder(root.right)
        
    def postOrder(self, root: TreeNode or None) -> None:
        if root == None: return
        
        self.postOrder(root.left)
        self.postOrder(root.right)
        print(root.val, end=" ")
        
tree = BST()
tree.insert(30)
tree.insert(50)
tree.insert(15)
tree.insert(20)
tree.insert(10)
tree.insert(40)
tree.insert(60)

root = tree.getRoot()

tree.preOrder(root)
print()

tree.inOrder(root)
print()

tree.postOrder(root)
print()
