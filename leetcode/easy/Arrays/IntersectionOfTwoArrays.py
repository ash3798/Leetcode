#approach : use hash map     Complexity = time: O(n)  space: O(n)
def findIntersection(arr1 , arr2) :
    #iterate over one array and fill its elements into hashmap
    res = []
    myDict = {}
    for num in arr1:
        if num in myDict :
            myDict[num] += 1
        else:
            myDict[num] = 1
    
    #iterate over second array to see which all elements are there in hashmap
    for num in arr2:
        if num in myDict:
            if myDict[num] > 0 :
                res.append(num)
                myDict[num] -= 1
    
    return res
    
#driver code
arr1 = [1,2,3,2,1]
arr2 = [1,2,2,5,1]
print(findIntersection(arr1 , arr2))


##################################################
#         #if arrays are in sorted form , optimizing for that
#         i = 0;
#         j = 0;
        
#         nums1.sort()
#         nums2.sort()
        
#         res = []
        
#         while i < len(nums1) and j < len(nums2) :
#             if nums1[i] == nums2[j] :
#                 res.append(nums1[i])
#                 i += 1
#                 j += 1
#             elif nums2[j] < nums1[i] :
#                 j += 1
#             elif nums2[j] > nums1[i] :
#                 i += 1
        
#         return res