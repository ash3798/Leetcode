class TreeNode:
  def __init__(self , value=0):
    self.data = value
    self.left = None
    self.right = None

def findMinPathSum(root , path , sum , min,minPath ):
  if root == None:
    return
  
  path.append(root.data)
  sum += root.data

  if root.left == None and root.right == None :
    if sum < min[0] :
      min[0] = sum
      minPath[0] = list(path)
    elif sum == min[0] :
      if len(path) > len(minPath) :
        min[0] = sum
        minPath[0] = list(path)

  findMinPathSum(root.left , path , sum , min , minPath)

  findMinPathSum(root.right , path, sum , min , minPath)
  
  path.pop()
  sum -= root.data


#calling code 
root = TreeNode(10)    #root of BST
root.left = TreeNode(5)
root.right = TreeNode(5)
#root.left.left = TreeNode(25)
root.left.right = TreeNode(-2)
#root.right.left = TreeNode(125)
root.right.right = TreeNode(1)
root.right.right.left = TreeNode(-1)

minPath = [[]]
min = [2**31-1]
findMinPathSum(root , [], 0, min , minPath)
print(min[0])
print(minPath[0])
