# approaches

#approach 1 :  inefficient (try for every node)             Complexity = time:O(n) | space = O(1) 


class TreeNode:
    def __init__(self,value , parent = None):
        self.data = value
        self.left = None
        self.right = None

def IsValidBST(node , min , max , size) :
    if node == None :
        return True

    size[0] += 1
    if node.data <= min or node.data >= max :
        return False

    return IsValidBST(node.left, min , node.data-1 ,size) and IsValidBST(node.right , node.data+1 , max , size)
    

def FindLargestIterativeWay(root):  #this is less efficient than recursive way as it always looks at all n node's subtree
    queue = [root]
    maxSize = 0

    while len(queue) != 0 :
        node = queue.pop()

        size = [0]
        IsValidBST(node  , -2**31 , 2**31-1, size)
        if size[0] > maxSize :
            maxSize = size[0]
        
        if node.left != None :
            queue.append(node.left)

        if node.right != None :
            queue.append(node.right)


    return (maxSize)


def largestBST(node) :
    size = [0]
    if IsValidBST(node  , -2**31 , 2**31-1, size) == True :
        return size[0]

    return max(largestBST(node.left) , largestBST(node.right))

def FindLargestRecursiveWay(root) :     #this is better than iterative as it first looks for root and if finds returns from there itself
    return largestBST(root)             #if it doesnt find , then only its gonna move forward with subtrees of that root

#calling code 
root = TreeNode(50)
root.right = TreeNode(60)
root.left = TreeNode(30)
root.left.right = TreeNode(20)
root.left.left = TreeNode(5)

root.right.left = TreeNode(45)
root.right.right = TreeNode(70)
root.right.right.left = TreeNode(65)
root.right.right.right = TreeNode(80)

print(FindLargestIterativeWay(root)) 

print(FindLargestRecursiveWay(root))