#best approach : bit manipulation
# we can use property of XOR 
#   ie  a XOR a = 0
#       a XOR 0 = a
def findSingle(nums):
    res = 0 
    for num in nums :
        #perform XOR on all the elements of array
        res = res ^ num
    return res

#driver
nums = [4,1,2,1,2,4,5]
print(findSingle(nums))

#======================================

#approach 1 : use mathematics   Complexity =  time : O(n) , space : O(n/2)
#iterate the array , add all unique numbers to hashmap
#then x = add all the numbers in hashmap and double
#then y = add all elements of given array 
#x-y  is the missing number 

#approach 2 : use the same principle as approach 1 but use set instead of hashmap

#approach 3 : we can fill hashtable with elements and their frequencies 
#then we can seewhich element appeared only once

#approach : brute force    Complexity =  time : O(n^2) , space : O(1)
#manually trying to find the duplicate for each element in array 
