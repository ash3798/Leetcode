#approaches

#approach 1 :           Complexity=  time:O(n) | space:O(n)
#find path for both targets , once found traverse both of then together and return element prev to mismatch


#approach 2 :           Complexity = time:O(n) | space:O(1)
#recursive approach to check that at which side of tree key is present and return node according to that


########################approach 2 #################################
class TreeNode:
    def __init__(self,value):
        self.data = value
        self.left = None
        self.right = None

def findLCA(root , t1 , t2) :
    if root == None :
        return None

    if root.data == t1 or root.data == t2 :
        return root.data

    leftLCA = findLCA(root.left, t1, t2)
    rightLCA = findLCA(root.right , t1 , t2)

    if leftLCA == None and rightLCA == None :
        return None

    if leftLCA != None and rightLCA != None :   #check if both are not NONE (means one one target on both sides)
        return root.data

    if leftLCA != None :    #check if both target is on left
        return leftLCA

    return rightLCA    #if not on left then both target is on right


#calling code 
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)

print(findLCA(root , 4 ,6))
print(findLCA(root , 4, 2))
print(findLCA(root , 4, 5))
print(findLCA(root , 3 ,4))


##############################approach 1 ###############################

# class TreeNode:
#     def __init__(self,value):
#         self.data = value
#         self.left = None
#         self.right = None

# def findPath(root , t , p) :
#     if root == None :
#         return False

#     p.append(root.data)
    
#     if root.data == t :
#         return True

#     if findPath(root.left, t ,p) == True:
#         return True

#     if findPath(root.right, t ,p) == True:
#         return True

#     p.pop()
#     return False
    

# def findLCA(root , t1 , t2):
#     p1 = []
#     p2 = []
#     findPath(root , t1, p1)
#     findPath(root , t2 , p2)

#     l = min(len(p1) , len(p2))
#     prev = -1

#     for i in range(l) :             #while loop can be used to with and condition checking lengths of both paths
#         if p1[i] != p2[i] :
#             break
#         prev = p1[i]

#     return prev

# #calling code 
# root = TreeNode(1)
# root.left = TreeNode(2)
# root.right = TreeNode(3)
# root.left.left = TreeNode(4)
# root.left.right = TreeNode(5)
# root.right.left = TreeNode(6)
# root.right.right = TreeNode(7)

# print(findLCA(root , 4 ,6))
# print(findLCA(root , 4, 2))
# print(findLCA(root , 4, 5))
# print(findLCA(root , 3 ,4))