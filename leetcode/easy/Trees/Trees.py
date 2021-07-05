class TreeNode:
    def __init__(self, val=0 , left= None , right = None):
        self.val = val
        self.left = left
        self.right = right

#check for corner cases like root = null , root is the only element in tree , only left is there or viceversa
#to find length of the tree , we need to find length of left subtree and right subtree => and then consider the maximum one
#use leaf node as base cases
def maxDepth(root):
    if root == None :
        return 0

    leftLen = maxDepth(root.left)
    rightLen = maxDepth(root.right)

    return max(leftLen , rightLen) + 1

########################valid BST###################
#corner cases : empty tree , onlu root present , single branch present , equal elements 
#additional tricky use case : all left values should be smaller than root and all right should be larger than root
#if we do just with the check that immediate children are fitting condition it will fail in some cases

#approach 1:  pass down the parent while calling for subtrees and make comparison to parent also
#               parent should be passed in such a way that we could determine if its left subtree or right ,  so that we can make comparison acc to that
# 
#approach 2 : use inorder traversal , and we should get a sorted arrau 
#                   to save space we can just keep track of previous encountered element and then compare to next element found 


####approach 2######
def isValidBST(root):
    lastNode = None
    def inorder(node) :
        global lastNode
        if node == None :
            return True

        if inorder(node.left) == False:
            return False

        if lastNode != None and lastNode.val >= node.val :
            return False

        lastNode = node 
        return inorder(node.right)
    
    return inorder(root)


####approach 1######
# def isValidBST(root , l , r):
#     if root == None :
#         return True

#     #value in the nodes that are left to root should be less than root
#     if l != None and root.val <=  l.val :  #condition should be acc to negetive scenario
#         return False

#     #value in the nodes that are right to the root should be greater than root    
#     if r != None and root.val >= r.val:
#         return False

#     validLeft = isValidBST(root.left , l , root)   #root is on the right of the left subtree 
#     validRight = isValidBST(root.right , root, r)   #root is on the left of the right subtree

#     return (validLeft and validRight)

#####below approach wont work in some cases (when max value in left subtree is greater that node itself  or min value in right subtree is less than node)
#def validBST(root ):
    # if root == None:
    #     return True

    # if root.left != None and root.left.val >= root.val:
    #     return False
    # if root.right != None and root.right.val <= root.val:
    #     return False

    # isValidLeft = validBST(root.left)
    # isValidRight = validBST(root.right)

    # return (isValidLeft and isValidRight)        

#############################################################

##################symmetric tree ############################
#need to identify if the left and right portion of the tree are symmetrical/mirror images
#corner cases : empty tree , only root node present

#approach 1 : recursive => traverse through all nodes of both trees and keep comparing along the way
#                       if left is taken for first tree , take right for other tree (since mirror images)
#                       add neccesary checks for values , as well as one tree's node being null and other's not
#approach 2 : iterative =>
#               use BFS to traverse through all nodes of both trees 
#               take two queues , one queue per tree
#               insert the nodes in queues in opposite order from each other (one from left , other from right)
#               make comparisons of the node values , when you dequeue the node
#note : put checks for node being null

#approach 1:
def isSymmetric(root) :
    def validate(node1 , node2):
        if node1 == None and node2 == None :  #check for null to remove null pointer exceptions
            return True

        if bool(node1) != bool(node2):    #check the status of both the nodes
            
            return False
        
        if node1.val != node2.val :
            return False
        
        if validate(node1.left , node2.right) == False :
            return False
        
        return validate(node1.right , node2.left)

    #corner case check
    if root == None:
        return True
    
    #call validate
    return validate(root.left , root.right)
        

################################################################################

########################Binary Tree level order traversal########################
#approach : Breadth first search (modified)
#             we will follow same process as the bfs but every time we dequeue the nodes of some level n and add it children (nodes of level n+1) to queue,
#              we will keep track of how many children got added from the nodes at level n , that will tell us number of the nodes at level n+1
#               once we can have that count , we can dequeue only that many nodes in next run and put them their values in array to add to the final result array
#               we will keep repeating this same process for all levels 
#           we can take help of nested loops to accomplish this.

#approach 2 : recursive mainly +small iteration 
#           very inefficient approach
#   find the max depth, then iterate from (maxdepth to 1)
#for each iteration , traverse the treee , when you find the node of that depth , add it to the temp array
#once all elements of that depth found , append it to final array 
#repeat same for all depths
#highly inefficient as we are traversing the whole tree again and again , but still getting nodes of single level


#approach 1 :
def levelOrder(root):
    if root == None :
        return []

    res = []

    q = deque()
    q.append(root)

    nodesOnLevel = 1
    while len(q) != 0 :
        noOfChildren = 0
        temp = []

        while nodesOnLevel != 0 :
            node = q.popleft()
            temp.append(node.val)

            #add children of popped node
            if node.left :
                q.append(node.left)
                noOfChildren += 1
            if node.right :
                q.append(node.right)
                noOfChildren += 1
            
            nodesOnLevel -= 1
        
        res.append(temp)
        nodesOnLevel = noOfChildren

    return res


#########################################################################

######################## Convert Sorted Array To height balanced binary Tree #####################
#approach : 
#corner case :  nums length is zero , nums length is one 
#   take the mid of the array to make the root of our tree
#       after that find the left and right children by finding the mid of the left and right portions
#   keep doing this , until all the nodes are placed onto the tree

def sortedArrayToBST(nums) :

    def findnode(nums , start , end) :
        if start > end :
            return None

        mid = (start + end)//2
        node = TreeNode(nums[mid])

        node.left = findnode(nums , start , mid-1)
        node.right = findnode(nums , mid+1 , end)

        return node

    #handle corner case
    if len(nums) == 0 :
        return None
    
    root = findnode(nums, 0 , len(nums)-1)
    return root