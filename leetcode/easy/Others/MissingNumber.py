#corner cases
#if n itself is missing  : need to handle this by calculating n using the length of array  (not by finding max)

#approach 1 : Sorting     complexity=  time:O(nlogn)   space:O(1)
# we can sort the array and then iterate over it to check which value is missing 


#approach 2 : Hashing    complexity=  time:O(n)     space:O(n)
# we can find n using length of array 
#we can iterate array and put all elements to hashmap
#now we can traverse range (0 to n) , to find out which element is missing 


#approach 3 : Gauss formula    Complexity= time:O(n)     space:O(1)
#we can find n using length of array 
#we can find the sum of range (0,n)  using gauss formula
# we can then iterate array to find the sum of array 
# subtract two sums and we get the missing value


#approach 4 : Bit manipulation(XOR)   Complexity= time:O(n)  space:O(1)
#we make use of the property of XOR ie  XOR of value with itself is zero and XOR with zero is value itself
#find n using the length of array
# do XOR of ( n ^ (index1^value1 .......indexn^valuen) )   for whole array
#if dont want to use indexes we can iterate the range(o,n) and XOR all the elements and just XOR values from array
# in the end you will be remaining with missing value


#######################################


# #approach 3 :
# def MissingNumber(nums):
#     n = len(nums)

#     expectedSum = (n*(n+1))//2
#     actualSum = 0
#     for num in nums:
#         actualSum += num

#     return expectedSum-actualSum

# #driver code
# nums=[2,0,1]
# print(MissingNumber(nums))



############################################

#approach 4 :
def MissingNumber(nums):
    n = len(nums)
    missing = n

    for i  in range(len(nums)) :
        missing = missing^i^nums[i]     #do XOR of all the indexes and values
                                        #if donot want to use indexes ,iterate  range(0,n) and XOR values
    return missing

#driver code
nums=[3,0,1]
print(MissingNumber(nums))