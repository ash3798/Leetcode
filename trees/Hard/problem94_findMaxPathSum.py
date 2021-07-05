class TreeNode:
    def __init__(self,value , parent = None):
        self.data = value
        self.left = None
        self.right = None

def findMaxSum(node , maxSum) :
    if node == None :
        return 0

    leftSum = findMaxSum(node.left , maxSum)
    rightSum = findMaxSum(node.right , maxSum)

    localSum = node.data + leftSum + rightSum
    if localSum > maxSum[0] :
        maxSum[0] = localSum

    return max(leftSum+node.data , rightSum+node.data , node.data)

#calling code
root = TreeNode(10)
root.right = TreeNode(10)
root.left = TreeNode(2)
root.left.right = TreeNode(1)
root.left.left = TreeNode(20)

root.right.right = TreeNode(-25)
root.right.right.left = TreeNode(3)
root.right.right.right = TreeNode(4)

maxSum = [0]
findMaxSum(root, maxSum)
print(maxSum[0])