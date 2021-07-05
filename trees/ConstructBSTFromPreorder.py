class TreeNode:
    def __init__(self, val=0 , left= None , right = None):
        self.val = val
        self.left = left
        self.right = right

def constructBSTFromPreorder(treeArr) :
    stack = []
    root = TreeNode(treeArr[0])

    stack.append(root)     #append root , first element in preorder is root always

    i = 1     #root already included
    while i < len(treeArr):

        while len(stack) >0 and treeArr[i] > stack[-1].data :
            temp = stack.pop()

        if temp != None :    #temp will be null in case no popping happened . either due to no element in stack or larger elements in stack
            temp.right = treeArr[i]
            stack.append(temp.right)

        else :               # treeArr[i] < stack[-1]   ,this case is put in else so that when stack is empty it wont raise the null exception
            temp = stack[-1]
            temp.left = TreeNode(treeArr[i])
            stack.append(temp.left)

        i += 1

    return root