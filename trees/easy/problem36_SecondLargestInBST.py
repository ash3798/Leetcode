class TreeNodeExt:
    def __init__(self,value , parent = None):
        self.data = value
        self.left = None
        self.right = None

def reverseInorder(node , c):
    if node == None :
        return False

    if reverseInorder(node.right , c) :
        return True

    c[0] += 1   #increment first and then read which element we are on
    if c[0] == 2:
        c[1] = node.data
        return True
        

    if reverseInorder(node.left , c) :
        return True    

    return False

#apporoach : reverse Inorder traversal
def findSecondLargestInBST(root) :
    c = [0]*2

    if reverseInorder(root , c) :
        return c[1]
    
    return "not found"


#driver code 
t1 = TreeNodeExt(100)
t2 = TreeNodeExt(50)
t3 = TreeNodeExt(150)
t4 = TreeNodeExt(25)
t5 = TreeNodeExt(115)

t1.left = t2
t1.right = t3

t2.parent = t1
t3.parent = t1

t2.left = t4
t4.parent = t2

t3.left = t5
t5.parent = t3

print(findSecondLargestInBST(t1))