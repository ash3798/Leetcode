class TreeNode:
    def __init__(self,value , parent = None):
        self.data = value
        self.left = None
        self.right = None

def evaluate(node) :
    if node.left==None and node.right == None :
        return node.data

    lvalue = evaluate(node.left)

    operand = node.data

    rvalue = evaluate(node.right)

    result = 0
    if operand == "*":
        result = lvalue * rvalue
    elif operand == "+" :
        result = lvalue + rvalue
    elif operand == "-" :
        result = lvalue - rvalue
    elif operand == "/" :
        result = lvalue / rvalue

    return result

#driver code
root = TreeNode("*")
root.left = TreeNode("+")
root.right = TreeNode("+")
root.left.left = TreeNode(3)
root.left.right = TreeNode(2)
root.right.left = TreeNode(4)
root.right.right = TreeNode(5)

print(evaluate(root))
