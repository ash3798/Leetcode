#approch :  we will move inorder and keep track of the previous visited node.  Use that prev visited node to attach the new nodes to linked list
#Note : make use of the sentinal node , in order to make the avoid special handlings for head

class TreeNode:
  def __init__(self, value =0):
    self.data = value
    self.left = None
    self.right = None

def BTreeToDLL(node , prevRef) :
  if node == None :
    return None

  BTreeToDLL(node.left , prevRef)

  prev = prevRef[0]
  prev.right = node
  node.left = prev
  
  prevRef[0] = node

  BTreeToDLL(node.right , prevRef)

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


sentinal = TreeNode(-1)
prevRef = [sentinal]
BTreeToDLL(root , prevRef)

DLLRoot = sentinal.right
DLLRoot.left = None

parseLinkedList(DLLRoot)
