#approach 1 :  early load  , complexity is O(n)  , n = number of nodes generated 

#approach 2 : lazy load . complexity is O(1) , full tree is not generated at once 
#it will get generated node by node when we refer them .
#involves modification to the way we call the left and right child of root

##################################approach 1 ###################
import random

class TreeNode:
    def __init__(self , value):
        self.data = value
        self.left = None
        self.right = None
        self.left_initiated = False
        self.right_initiated = False

def generate():
    root = TreeNode(0)
    return root


def left(root):
    if not root.left_initiated:
        if random.random() < 0.5:
            root.left = generate()
        root.left_initated = True
    return root.left

def right(root):
    if not root.right_initiated:
        if random.random() < 0.5:
            root.right = generate()
        root.right_initiated = True
    return root.right

def traverse(root):
    if root == None:
        return None

    traverse(left(root))
    print(root.data)
    traverse(right(root))


#calling code
root = generate()
traverse(root)



########################approach 1 ##########################

# import random

# class TreeNode:
#     def __init__(self, value = 0):
#         self.data = value
#         self.left = None
#         self.right = None
# def generate() :
#     root = TreeNode(0)

#     if random.random() > 0.5 :
#         root.left = generate()
    
#     if random.random() > 0.5 :
#         root.right = generate()

#     return root

# def traverseTree(root) :
#     if root == None :
#         return

#     traverseTree(root.left)
#     print(root.data)
#     traverseTree(root.right)

# #calling code
# root = generate()
# traverseTree(root)