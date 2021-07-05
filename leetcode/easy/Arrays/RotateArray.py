#approach 1  complexity :  time : O(n)   space : O(1) 
def reverse(nums , start , end) :
    while start < end :
        nums[start] , nums[end] = nums[end] , nums[start]
        start += 1
        end -= 1

#reverse it 3 times , 
#one time full array , then both partitions on sides of k index indivisually
def rotate (nums , k) :
    reverse(nums , 0 , len(nums)-1)

    reverse(nums , 0 , k-1)
    reverse(nums , k , len(nums)-1)

#driver code
nums  = [-1,-100,3,99]
k = 2
rotate(nums , k)
print(nums)

#approach complexity :  time : O(n)   space : O(n)
# in this we can leverage either hashmap or new array to put elements at final position 

#approach complexity :  time : O(n*k)   space : O(1) 
#rotate our array k times each time pushing elements one place forward