#approach 0 = store the replaced element and update index ...    Complexity = time :O(n) | space : O(1)
def rotate(nums, k) :
    n = len(nums)
    num_elements = 0

    i = 0
    
    while num_elements < n :
        next_pos = (i +k ) % n
        last_ele = nums[i]

        while True :
            temp = nums[next_pos]
            nums[next_pos] = last_ele
            last_ele = temp

            num_elements += 1

            next_pos = (next_pos + k) % n

            if next_pos == (i+k)%n :
                break
        i+=1

#driver code
nums  = [1,2,3,4,5,6,7]
k = 3
rotate(nums , k)
print(nums)

####################################################################
# #approach 1  complexity :  time : O(n)   space : O(1) 
# def reverse(nums , start , end) :
#     while start < end :
#         nums[start] , nums[end] = nums[end] , nums[start]
#         start += 1
#         end -= 1

# #reverse it 3 times , 
# #one time full array , then both partitions on sides of k index indivisually
# def rotate (nums , k) :
#     reverse(nums , 0 , len(nums)-1)

#     reverse(nums , 0 , k-1)
#     reverse(nums , k , len(nums)-1)

# #driver code
# nums  = [-1,-100,3,99]
# k = 2
# rotate(nums , k)
# print(nums)

###################################################################
#approach 2   complexity :  time : O(n)   space : O(n)
# in this we can leverage either hashmap or new array to put elements at final position 

#approach 3  complexity :  time : O(n*k)   space : O(1) 
#rotate our array k times each time pushing elements one place forward