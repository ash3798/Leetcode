class TreeNode:
    def __init__(self,value , parent = None):
        self.data = value
        self.left = None
        self.right = None

def findDeepest(node , currDepth , max):
    if node == None :
        return
    if node.left ==None and node.right ==None :
        if currDepth > max[0] :
            max[0] = currDepth
            max[1] = node.data
    else :
        findDeepest(node.left , currDepth+1 , max)
        findDeepest(node.right , currDepth+1 , max)

#driver code 
root = TreeNode("a")
root.left = TreeNode("b")
root.right = TreeNode("c")
root.left.left = TreeNode("d")
root.left.left.right = TreeNode("e")
root.left.left.right.left = TreeNode("f")

max = [0 , "0"]       #max[0] will be max depth ,  max[1] will be the max element

findDeepest(root , 0 , max)
print(max[1])
