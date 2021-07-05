#also called as Hamming weight

#approach 1 : Use Mask          Complexity : time:(O(1)) , as it will be 32 operations always
# we will take a mask and evaluate one bit of n at a time .
#we will start from least significant bit and compare (ie mask = 1) 
# then shift the mask right to check second last bit and so one
# we can say n has one bit if ( n & mask ) != 0 


#approach 2 : Use the property that decrementing number will flip the least significant 1 bit of n
#Complexity : time:(O(1)) , as it will be 32 operations always
#we will keep doing  (n & n-1 ) until n becomes zero .
#number of steps that it takes to make n zero will be equal to number of 1 bits in n



# #approach 1 :
# def countOneBits(n : int):
#     mask = 1        #mask should be set = 1 initially as we keep shifting this 1 in subsequent iterations
#     oneBits = 0
    
#     for i in range(32) :
#         if n&mask != 0:         # result will be !=0 if n also have 1 bit at that place corresponding to mask
#             oneBits += 1
        
#         mask = mask << 1    #shift mask by one

#     return oneBits

# #driver code 
# n =  11
# print(countOneBits(n))

#####################################

#approach 2 :
def countOneBits(n : int) :
    oneBits = 0

    while n != 0 :
        n = n & (n-1) 
        oneBits += 1
    
    return oneBits

#driver code 
n =  15
print(countOneBits(n))