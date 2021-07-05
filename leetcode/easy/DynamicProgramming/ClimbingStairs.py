#corner cases:   value of n(total num of stairs) is zero

#approachs :

#approach 1: brute force    time :O(2^n)   space:O(n)
#   in this we will try to see each and every possible combination
#   we will try all our possible steps at every n  ie from 0 to n


#approach 2 : memoization(improved version of brute force)    time: O(n)   space:O(n)
#   it will be the same process as the brute force 
#   we will keep one table now to lookup , in order to not avoid same calculations


#approach 3 : bottom up DP     time:O(n)    space: O(n)
#   we will fill up the dp table in bottom up fashion
#   we can get to ith step from either i-1th or i-2th step
#   we can take base case of 0 steps here and keep building our dp by using the same process as above line



# #approch 1:
# def climbstairs(i , n):
#     if i > n :
#         return 0

#     if i == n:
#         return 1

#     return climbstairs(i+1 , n) + climbstairs(i+2 , n)

# #driver code
# n = 2
# print(climbstairs(0 , n))


###############################

# #approach 2 :
# def climbstairs(i ,n , memo) :
#     if i >n :
#         return 0
#     if i == n :
#         return 1

#     if memo[i] > 0 :
#         return memo[i]

#     memo[i] = climbstairs(i+1 , n , memo) + climbstairs(i+2 , n , memo)
#     return memo[i]

# #drivercode
# n =5
# memo = [0] * (n+1)

# print(climbstairs(0 , n , memo))


########################################

#approach 3 :
def climbstairs(n):
    dp = [0]*(n+1)

    dp[0] = 1   #only one way for 0 steps i.e take no steps

    i = 1 
    while i <= n :
        totalways = 0
        if i-1 >=0 :
            totalways += dp[i-1]
        if i-2 >= 0 :
            totalways += dp[i-2]
        
        dp[i] = totalways
        i += 1

    return dp[n]