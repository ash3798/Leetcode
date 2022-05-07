class TreeNode:
  def __init__(self , value=0):
    self.data = value
    self.left = None
    self.right = None

from collections import deque

def findMinimumSum(root):
  if root == None :
    return 0

  currLvl = 0
  smallestSumLevel = -1
  currLvlCnt = 1
  minSum = (2**31)-1
  q = deque()
  q.append(root)

  while len(q) != 0 :
    childCount = 0
    localSum = 0

    while currLvlCnt > 0 :
      node = q.popleft()
      localSum += node.data

      if node.left != None :
        q.append(node.left)
        childCount += 1

      if node.right != None :
        q.append(node.right)
        childCount += 1

      currLvlCnt -= 1

    if minSum > localSum :
      minSum = localSum
      smallestSumLevel = currLvl

    currLvlCnt = childCount
    currLvl += 1

  return smallestSumLevel


#calling code 
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(-5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(-7)

print(findMinimumSum(root))
