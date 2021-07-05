class TreeNode:
    def __init__(self, val=0 , left= None , right = None):
        self.val = val
        self.left = left
        self.right = right

# def invert(node):
#     if node == None :
#         return 

#     node.left , node.right = node.right , node.left

#     #recursively apply same process to whole left and right subtree
#     invert(node.left)
#     invert(node.right)    

def inorder(node , inord):
    if node == None :
        return

    inorder(node.left , inord)
    inord.append(node.val)
    inorder(node.right , inord)

# #driver code
# root = None
# # root = TreeNode(0)
# # root.left = TreeNode(3)
# # root.right = TreeNode(2)
# # root.right.left= TreeNode(5)
# # root.right.right= TreeNode(4)

# root= TreeNode(1)
# root.left= TreeNode(2)
# root.left.left= TreeNode(3)
# root.left.left.left= TreeNode(4)
# root.left.left.left.left= TreeNode(5)

# inord = []
# inorder(root, inord)
# print(inord)

# invert(root)
# inord = []
# inorder(root, inord)
# print(inord)

#########################################################
#approach 2 : iterative approach
def invert(root) :
    if root == None :
        return None
    
    q = [root]

    while len(q) != 0:
        node = q.pop(0)
        
        #swap the children 
        node.left , node.right = node.right , node.left

        if node.left != None :
            q.append(node.left)
        if node.right != None :
            q.append(node.right)

#driver code
root = None
# root = TreeNode(0)
# root.left = TreeNode(3)
# root.right = TreeNode(2)
# root.right.left= TreeNode(5)
# root.right.right= TreeNode(4)

root= TreeNode(1)
root.left= TreeNode(2)
root.left.left= TreeNode(3)
root.left.left.left= TreeNode(4)
root.left.left.left.left= TreeNode(5)

inord = []
inorder(root, inord)
print(inord)

invert(root)
inord = []
inorder(root, inord)
print(inord)

    