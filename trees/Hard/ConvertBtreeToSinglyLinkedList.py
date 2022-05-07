#recursive approach here , make the root tree point towards the left and left point towards the right, recursively this should be
# done on left as well as right subtree

class TreeNode:
  def __init__(self, value =0):
    self.data = value
    self.left = None
    self.right = None

def flatten(node) : 
  if node == None :
    return node

  if node.left != None :
    flatten(node.left)    #flatten left subtree to ll first
    
    tempRight = node.right
    node.right = node.left

    curr = node.right
    while curr.right != None :
      curr = curr.right
    
    curr.right = tempRight      #will attack last node of flattened left subtree to right side of prev level tree

    flatten(curr.right)   #flatten right side to ll

  else:  #seperate handling if left child is not present
    flatten(node.right)

  return node

def parseLinkedList(head):
  curr = head   
  while curr != None :
    print(curr.data)
    curr = curr.right

#calling code
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)

llHead = flatten(root)
parseLinkedList(llHead)
