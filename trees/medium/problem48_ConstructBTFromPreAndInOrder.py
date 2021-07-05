class TreeNode:
    def __init__(self,value , parent = None):
        self.data = value
        self.left = None
        self.right = None

def FillNodes(preorder , inorderMap,start , end , c):
    if start > end :
        return None

    preidx = c[0]
    inidx = -1

    if preorder[preidx] in inorderMap:
        inidx = inorderMap[preorder[preidx]]

    if  inidx < start or  inidx > end :
        return None

    node = TreeNode(preorder[preidx])
    c[0] += 1

    if start == end :
        return node 
        
    node.left = FillNodes(preorder , inorderMap, start , inidx-1 ,c)
    node.right = FillNodes(preorder , inorderMap , inidx+1 , end , c)

    return node

def constructTree(preorder , inorder):
    if len(preorder) == 0  or len(inorder) == 0 :
        return None

    inorderMap = dict()
    for i in range(len(inorder)) :      #since this is using dict , it wont handle duplicates
        inorderMap[inorder[i]] = i

    c = [0]
    root = FillNodes(preorder , inorderMap,0 , len(preorder)-1 ,c) #c is just for tracking the curr preorder index

    return root

def parseTree(root):
    if root == None:
        return
    
    print(root.data)
    parseTree(root.left)
    parseTree(root.right)

#driver code 
preorder = [100, 50 , 25 , 150 , 115]
inorder = [25 , 50 , 100 , 115 , 150]

root = constructTree(preorder , inorder)
parseTree(root)
