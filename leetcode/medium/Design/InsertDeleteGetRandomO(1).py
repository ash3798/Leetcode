#aim is to make insert , delete and random operation as O(1) time complexity

#approach 1 :  brute force
# we can use map to store new values , 
#this will give us the o(1) insert and delete
#but for getting random val from the map will take O(n) complexity



#approach 2 : optimized  O(1) approach 
#here we will tradeoff space for more performance 
#   take a array to store the all the values 
#   we take length variable to track our length
#   take one hashmap to store the  <values : index in arr>  pairs
# insert will be O(1) , for both map and arr
#for random selection, we will use our length variable to select one random val from 0 to length and return val at that index
# Removal is not straight forward , as removal from mid will cost us O(n)
# To overcome this:
#   for removal , we will identify thr index using our map => overwrite that index with the last element of arr 
#   =>now we can pop off last element as it is O(1) cost => also modify the index of that last element in map also
#   => remove the entry of target val from map  => decrement the length variable also 