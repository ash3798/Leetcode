class TreeNode:
    def __init__(self,value , parent = None):
        self.data = value
        self.left = None
        self.right = None

def calcHeight(node) :
    if node == None :
        return 0
    return max(calcHeight(node.left) ,  calcHeight(node.right))+1

def printLevel(node , level):
    if node == None :
        return
        
    if level == 0 :
        print(node.data, end =" ")
        return

    printLevel(node.left , level-1)
    printLevel(node.right , level-1)

def printTreeLevels(root) :
    height = calcHeight(root)

    for i in range(height) :
        printLevel(root , i)
        print("")


#calling code
#calling code
root = TreeNode(10)
root.right = TreeNode(10)
root.left = TreeNode(2)
root.left.right = TreeNode(1)
root.left.left = TreeNode(20)

root.right.right = TreeNode(-25)
root.right.right.left = TreeNode(3)
root.right.right.right = TreeNode(4)
printTreeLevels(root)