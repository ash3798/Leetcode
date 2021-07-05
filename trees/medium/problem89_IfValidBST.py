class TreeNode:
    def __init__(self,value , parent = None):
        self.data = value
        self.left = None
        self.right = None

def IsValidBST(node , min , max) :
    if node == None :
        return True

    if node.data <= min or node.data >= max :
        return False

    return IsValidBST(node.left, min , node.data-1) and IsValidBST(node.right , node.data+1 , max)
    

#driver code 
root = TreeNode(100)
root.right = TreeNode(150)
root.left = TreeNode(50)
root.left.right = TreeNode(75)
root.right.left = TreeNode(90)

print(IsValidBST(root , -2**31 , 2**31-1))