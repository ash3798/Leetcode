#corner cases :  no house present , only one house present

#approach: Dynamic programming
#for every node we will compute the largest sum we could rob , alternative house should not be removed 
#so we need to find the max of (largest sum till(i-1) , largest sum till (i-2) + house[i])
def rob(nums):
    if len(nums) == 0 :
        return 0
    if len(nums) == 1 :
        return nums[0]

    dp = [0]*len(nums)
    # dp[0] = nums[0]
    # dp[1] = max(nums[0], nums[1])

    for i in range(0 , len(nums)):
        tmp = 0                   
        if i-2 >= 0 :            #two options here , either fill the dp array till first two elements or have handling for i-2 inside loop
            tmp = dp[i-2]
        else :
            tmp =0

        dp[i] = max(dp[i-1] , nums[i] + tmp)
    
    return dp[len(nums)-1]


#driver code 
nums= [1,2,3,1]
print(rob(nums))