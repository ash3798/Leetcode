#approach : 2 pointer approach with swap    Complexity = time:O(n)   space: O(1)
def MoveZeroes(nums) :
    i = 0
    j = 0

    #iterate whole array , if non zero element encountered swap it with i index element
    while j < len(nums) :
        if nums[j] != 0 :
            nums[j] , nums[i] = nums[i] , nums[j]
            i += 1
        
        j += 1

#driver code
nums = [0,1,1,1,1]
MoveZeroes(nums)
print(nums)


#approach : 2 pointer with overwrite  Complexity = time:O(n)   space: O(1)
#we can overwrite all non zero elements to front and then put zeros at rem places

#the wheather swapping or overwrite is better , it totally depends upon the use case
#in case like [0,1,1,1,1]  , overwrite is gonna perform better 
#   as overwrite = n write ops
#   in swapping = 2*n write ops


#approach : Using the extra array  Complexity = time:O(n)  space:O(n)