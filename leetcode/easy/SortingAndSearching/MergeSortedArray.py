#corner cases :
# second array could be empty

#approaches : inplace merging
#   here first array is bigger and has extra space to accomodate the elements from second array 
#   these extra spaces are filled with the dummy zero values
#       we can make use of this fact and start to fill the array from the end , so that we wont have to overwrite any of the previously stored elements
#       and by the time we reach the elements present previously they would already have gotten processed and no harm in overwriting them

#   just put a check on the pointers for new elements and prev elements ,  they should not be equal this implies that elements have already been processed

def merge(nums1  , m , nums2 , n) :
    #corner case n = 0 is handled already as none of the loops will run
    i = m-1
    j = n-1 
    k = m+n-1    #pointer for putting elements into final position from ending to start 

    while i>=0 and j >=0 :
        if nums1[i] > nums2[j] :
            nums1[k] = nums1[i]
            i -= 1
        else :
            nums1[k] = nums2[j]
            j -= 1
        
        k -= 1

    while j >= 0 :
        nums1[k] = nums2[j]
        j -= 1 
        k -= 1

#brute force : 
#   to compare elements of both array one by one , and then if some num from array 2 needs to be inserted , then
#   we will shift all the elements in arr1 from the point of insertion to end to make space for new entry 
#   without disrupting the order of the existing elements 

#approach : using new array and then merge the elements in there 
#but cant be used here since no extra space should be used 