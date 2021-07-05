#Complete tree are the ones where all the levels are completely filled , except for the last level and there also all the nodes will be as left as possible

#To store these types of trees , just the level order traversal is sufficient .
#and then we can find out the children for each node using formula :   leftchild = 2*i +1    , rightchild = 2*i +2 , where i is index of the parent in arr.