#corner cases 
#root can be null

#approach 1 : use Preorder traversal with storing nulls            Complexity :time = O(n) , n= number of entries in pre (nodes + nulls)  
#             Complexity = space: space taken up by preorder array (will be greater than no of nodes , as nulls are also included along with nodes)
# 
# to SERIALIZE the binary tree , we will use the prorder traversal .  create the array out of it and serialize it 
# DESERIALIZE :
#   we will use the preorder array we have and recursion to create tree 
#   iterate over the whole pre array , and create the node using the value of the current index in preorder
#   once node is created we will recursively fill its left and right also 
#   BASE CASE :
#       if the index goes beyond the len of preorder
#       if the element at current index is a marker for null (we can use a unique value to denote null )


##################

#approach 2 : preorder traversal with space optimizations   

# here it will be same as approach one , but instead of adding nulls we will try to add bits in our preorder to identify if it is leaf node or internal node
#if internal node :
#   we need to fill the left and rights 
#if leaf node :
#   we can skip filling left and right 

#also need to have unique symbol to identify , if in internal nodes one child is null 
# eg A'B'DE'G/C'/F    here, ' tell previous val is internal node ,   / tells null value of child in internal node ,   and values without ' are leaf nodes.