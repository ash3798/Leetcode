class TreeNode:
    def __init__(self, value = 0):
        self.data = value
        self.left = None
        self.right = None

def findPath(node , path , allPath) :
    if node == None :
        return
    
    if node.left == None and node.right == None :   #check if a leaf node
        path.append(node.data)
        allPath.append(list(path))
        path.pop()
        return

    path.append(node.data)

    if node.left != None :
        findPath(node.left , path , allPath)

    if node.right != None :
        findPath(node.right , path , allPath)

    path.pop()

#calling code
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
# root.right.left = TreeNode(4)
root.right.right = TreeNode(5)

path = []
allPath = []

findPath(root , path , allPath)
print(allPath)