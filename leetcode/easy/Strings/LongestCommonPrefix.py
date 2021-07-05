#horizontal scanning
    #in horizontal scanning , we are taking two elements at time ,comparing them and find the common prefix
    #once prefix is found , take that third element and find the commmon prefix between prev prefix and third element
    #keep going like this untill you have covered all the strings 
    #in the end you will have the largest common prefix

#vertical scanning
    #we will compare the first element of all the strings present in array 
    #if match found , we will compare second string and then third .....
    #this will continue till we find a mismatch or one of the strings in array ends
    #after this we will get the LCP of array 


#divide and conquer     time:O(2*n/2  * m ) = O(m.n)      space:O(m logn) extra space for recursion tree
    #use the associative property of LCP :   LCP(s1.....sn) = LCP( LCP(1...k) ,LCP(k+1.......n) )
    #we can find the mid of the array and try to process both the portions seperately.(make recursive call for both)
    #once both portions get computed , we can find the LCP between then for the answer
    #here base case for recusion will be { left==right , return s[left] }   LCP of single element is that element itself 


#binary search      time:O(S.logm)  s= m.n       space = O(1)
    #first find the len of smallest string in array 
    #now we apply the binary search kind of btw 0 to minLen
    #once mid found , take the value of prefix str[0][0 to mid]   and match it all the strings in the array
    #two outcomes possible :
        #it matches all the strings :  then change left = mid+1
        #it does not match : then change right = mid-1
    #base case for above is left <= right

    #once the loop ends mid of final left and right  ie.  (left+right)/2   ,, till this index the LCP is there
