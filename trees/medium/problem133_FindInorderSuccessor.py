#approach 1 : use parent node ,    Complexity = time O(h) | space:O(1)

#approach 2 : if not parent node given , Complexity  = time O(h) | space:O(1)


#############appraoch 2 #########################
class TreeNode:
  def __init__(self , value=0, parent = None):
    self.data = value
    self.left = None
    self.right = None
    self.parent = parent

def insert(root ,value):
  if root == None :
      return TreeNode(value)
  else:
    
    if value < root.data :
      temp = insert(root.left , value)
      root.left = temp
      temp.parent = root
    else :
      temp = insert(root.right , value)
      root.right = temp
      temp.parent = root
   
    return root


def findInorderSuccessor(node) :
  if node == None :
    return None

  #if right child is present for node
  if node.right != None :
    curr = node.right
    while curr != None and curr.left != None :
      curr = curr.left
    return curr.data
  
  succ = None
  #if right child is not present for node
  curr = root
  while curr != None :
    if curr.data < node.data :
      curr = curr.right
    elif curr.data > node.data :
      succ = curr
      curr = curr.left
    elif curr.data == node.data :
      break

  return succ.data

#calling node
root = None
 
# Creating the tree given in the above diagram
root = insert(root, 20)
root = insert(root, 8);
root = insert(root, 22);
root = insert(root, 4);
root = insert(root, 12);
root = insert(root, 10); 
root = insert(root, 14);  
#root = insert(root, 11); 
temp = root.left.right.right

print(findInorderSuccessor(root.left.right.left))


###################approach 1#########################
# class TreeNode:
#   def __init__(self , value=0, parent = None):
#     self.data = value
#     self.left = None
#     self.right = None
#     self.parent = parent

# def insert(root ,value):
#   if root == None :
#       return TreeNode(value)
#   else:
    
#     if value < root.data :
#       temp = insert(root.left , value)
#       root.left = temp
#       temp.parent = root
#     else :
#       temp = insert(root.right , value)
#       root.right = temp
#       temp.parent = root
   
#     return root

# def findInorderSuccessor(node) :
#   if node == None :
#     return None

#   if node.right != None : #means its internal node
#     curr = node.right

#     while curr != None and curr.left != None:
#       curr= curr.left
    
#     return curr.data

  
#   parent = node.parent

#   #scenario if a leaf node and is left child or right child
#   if parent.left == node :
#     return parent.data
#   elif parent.right == node :
#     curr = parent

#     while curr != None :
#       par = curr.parent
#       if par == None:
#         return None
      
#       if par.left == curr :
#         return par.data
#       else :
#         curr = par


# #calling node
# root = None
 
# # Creating the tree given in the above diagram
# root = insert(root, 20)
# root = insert(root, 8);
# root = insert(root, 22);
# root = insert(root, 4);
# root = insert(root, 12);
# root = insert(root, 10); 
# root = insert(root, 14);  
# root = insert(root, 11); 
# temp = root.left.right.right

# print(findInorderSuccessor(root.left.right.left.right))