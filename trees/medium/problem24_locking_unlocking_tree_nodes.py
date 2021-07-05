class TreeNodeExt():
    def __init__(self,value , parent = None):
        self.parent = parent
        self.data = value
        self.left = None
        self.right = None
        self.isLocked = False
        self.descLockedCount = 0


def isLocked(node):
    if node.isLocked :
        return True
    
    return False

def Lock(node):
    if node.isLocked :
        return False

    if node.descLockedCount > 0 :
        return False

    flag = False
    curr = node.parent
    while curr != None :
        if curr.isLocked :
            flag = True
            break
        curr = curr.parent
    
    if flag :
        return False
    
    node.isLocked = True
    
    curr = node.parent
    while curr != None :
        curr.descLockedCount += 1
        curr = curr.parent

    return True

def Unlock(node) :
    if not node.isLocked :
        return False 

    node.isLocked = False
    curr = node.parent
    while curr != None :
        curr.descLockedCount -= 1
        curr = curr.parent

    return True    

def parseTree(root):
    if root == None:
        return
    
    print(root.data ," " , root.descLockedCount , "  ", root.isLocked)
    parseTree(root.left)
    parseTree(root.right)

#driver code 
t1 = TreeNodeExt(1)
t2 = TreeNodeExt(2)
t3 = TreeNodeExt(3)
t4 = TreeNodeExt(4)
t5 = TreeNodeExt(5)

t1.left = t2
t1.right = t3

t2.parent = t1
t3.parent = t1

t2.left = t4
t4.parent = t2

t3.left = t5
t5.parent = t3

parseTree(t1)
print(Lock(t4))
parseTree(t1)
print(Lock(t2))

print(Lock(t5))
parseTree(t1)
print(Unlock(t4))

parseTree(t1)

print(Lock(t2))