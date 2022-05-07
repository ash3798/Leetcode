#problem : find the pair of nodes in BST which have sum equal to given target

#approaches :

#approach 1 : convert tree to inorder array and find pair       Complexity : time :O(n) | space :O(n)

#approach 2 : simultaneously do the inorder and reverse inorder traversal getting one value at a time from both and make further iterations according to their sum
#kinda like two pointer approach
#Complexity :   time:O(n) | space : O(log n)


class TreeNode:
  def __init__(self , value=0):
    self.data = value
    self.left = None
    self.right = None

def findPair(root , target) :
  if root == None:
    print("not found")
    return
  
  #stack will take just O(log n) space at max because only nodes in height of tree needs to be stored at point in time 
  s1 = [] #stack for normal inorder
  s2 = [] #stack for reverse inorder

  runNormal = True
  runReverse = True

  currNor = root
  currRev = root
  v1 = -1
  v2 = -1


  while(True):
    #normal inorder
    while runNormal :
      while currNor != None :
        s1.append(currNor)
        currNor = currNor.left            
      
      node = s1.pop()
      v1 = node.data
      runNormal = False
      currNor = node.right

    #reverse inorder
    while runReverse :
      while currRev != None :
        s2.append(currRev)
        currRev = currRev.right

      nodeR = s2.pop()
      v2 = nodeR.data
      currRev = nodeR.left
      runReverse = False
      

    if v1 > v2 :
      print("not found")
      break

    if v1 + v2 == target:
      print("pair is :" , v1 , "," , v2)
      return
    elif v1+v2 < target :
      runNormal = True
    elif v1+v2 >target :
      runReverse = True


#calling code 
root = TreeNode(100)    #root of BST
root.left = TreeNode(50)
root.right = TreeNode(150)
root.left.left = TreeNode(25)
root.left.right = TreeNode(75)
root.right.left = TreeNode(125)
root.right.right = TreeNode(175)

target = 100
findPair(root , target)
