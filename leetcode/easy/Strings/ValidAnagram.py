#approach : Using hashmap      Complexity : time:O(n)   space:O(n)
#same as below , but we will use hashmap to give more flexibility in terms of the input range
#will work even if we have Unicode inputs


#approach : creating a array to keep track if freq of chars      Complexity: time:O(n)  space:O(1)  // but with limitation that just alphabets we can work with
# a constant size (26) array we will create to denote all the alphabets .
# we can then iterate other array also to see if any freq goes down 0 . if it goes not anagram


#approach : sorting         Complexity : time:O(n logn)    space:O(1)  
#we can sort both strings , they should become similar after sorting 
#if they are similar , then they are anagram . otherwise not
