#approaches

#approach 1 :      Complexity : time:O(1)      space:O(1)
#we will make use of bitwise operations to reverse the bits
#we will take the left most or least significant bit of n  by doing (n&1)
#result from above step will result in just that bit being set and rest will be zero
#we can now try to put that bit in correct position as it will be in final result
#we can acheive this by shifting that bit by correct no of places ie (1st bit should go to 32nd place, 2nd to 31st etc)
#we can have a var ans=0 to store final result . we can do ans|res from prev command and insert our bit to 
# correct postion in final answer 
#keep repeating this until n is zero


#approach 2 : optimized for more number of requests
#complexity : time:O(1)  countable number of operations only
#             space:O(1)  as max numebr of combos for byte can be 2^8 = 256 , therefore cache space is constant in propotion to n
#Since caching is there , at some point in time cache will have all possible combos and we wont need to compute
# approach will stay same as approach 1 , but we will try to perform operation byte by byte instead of bit
#also we will introduce memoization to stop redundant calculations
#we will select whole byte , reverse it  and then try to place it at correct position as per final answer by shifting it
# we will first refer to memo if its miss , then only go ahead and compute. 

#####################################
# #approach 1
# def ReverseBits(n):
#     ans = 0
#     shiftval = 31       #shift value needs to be set carefully
#     while n > 0 :
#         tmp = n&1
#         tmp = tmp << shiftval     #assign it to var after shifting , var itself won't get modified by shift it just return values
#         shiftval -= 1
#         ans = ans|tmp

#         n =n >>1

#     return ans

# #driver code 
# n = 4294967293
# print(ReverseBits(n))

##############################

#approach 2:
def ReverseBits(n):
    def reverse(byte, cache):   #modified approach 1 to reverse a single byte instead of 32 bit
        if byte in cache :
            return cache[byte]    #if cachehit refer to cache for result

        ans = 0
        shiftval = 7      #shift value needs to be set carefully
        while byte > 0 :
            tmp = byte&1
            tmp = tmp << shiftval     #assign it to var after shifting , var itself won't get modified by shift it just return values
            shiftval -= 1
            ans = ans|tmp

            byte =byte >>1
        return ans


    shiftval = 24         #as shifting 24 in beginning will get our byte to correct position
    ans1 = 0
    cache = dict()
    while n > 0:
        tmp = n&0xff    #equivalent to ff
        tmpres = reverse(tmp,cache)

        tmpres = tmpres << shiftval
        shiftval -= 8

        ans1 = ans1|tmpres
        n = n>>8
    
    return ans1

#driver code 
n = 4294967293
print(ReverseBits(n))



#approach 3 : still need to understand

# def reverseBits(self, n):
#     n = (n >> 16) | (n << 16)
#     n = ((n & 0xff00ff00) >> 8) | ((n & 0x00ff00ff) << 8)
#     n = ((n & 0xf0f0f0f0) >> 4) | ((n & 0x0f0f0f0f) << 4)
#     n = ((n & 0xcccccccc) >> 2) | ((n & 0x33333333) << 2)
#     n = ((n & 0xaaaaaaaa) >> 1) | ((n & 0x55555555) << 1)
#     return n