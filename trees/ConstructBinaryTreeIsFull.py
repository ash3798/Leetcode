# pseudocode for creating a full binary tree  using preorder array

# full binary tree means nodes will have either 0 or 2 children
# here we are making use of that fact and  node in array should have some way to tell if its a leaf node or internal node


#########################################
#PREREQUISITE : our array should have values stored in such a manner that , it represents if the node is leaf node or internal node

##start of pseudocode
# arr = array of preorder traversal

# stack = empty array for stack 

# root = arr[0]   #as first value if from root in preorder 
# push root to stack 

# i = 1
# while i < length(arr)

#     if  stack.top.left == Null 
#         stack.top.left = TreeNode(arr[i])    #create node from the value
        
#         if stack.top.left is internal node          #if node is internal push it to stack , to process its subtree also
#             push stack.top.left to stack            #if node is leaf node ,dont push to stack

#     else if stack.top.right == Null
#         stack.top.left = TreeNode(arr[i]) 

#         if stack.top.right is internal node
#             push stack.top.right to stack       

#         pop the top element of stack       #because both the nodes of the top element have been filled already

# return root