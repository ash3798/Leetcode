#corner case : empty array, single element

#approach :
#approach 1 : brute force     time : O(n^2)
#we need to consider subarray (contigeous)  time : O(n^2),    not subset total:2^n subsets
#we need to take all the possible subarrays and see which one has the largest sum
#we can iterate element wise  
#  eg in below subarrays could be  [1],[1,2],[1,2,3]    , [2] [2,3]   , [3] 
#    1 , 2 , 3 


#approach 2 : Kadane's Algorithm          time : O(n^2)
# in this we try to calculate local max sums subarrays that will include current index and
#  then keep track of what was the largest sum that we got in subarrays

#eg  1,2,3,4
#   here  max sum subarray that includes 3 could be   [3] [3,2] [3,2,1]


#approach 3 : optimized Kadane's Algorithm with DP      time :O(n)
#same process as the kadane's algorithm 
#but when we find the maximum subarray for a index  , we will store it and use for future reference so that no recalculations is needed

def maxSubArray(nums) :
    maxsum_global = nums[0]
    maxsum_local = nums[0]

    for i in range(1, len(nums)):
        maxsum_local = max(nums[i] , nums[i]+maxsum_local)   #to optimise space , just stored the maxsum of subarray including element i-1 in variable rather than keeping track in lookup array

        if maxsum_local > maxsum_global :
            maxsum_global = maxsum_local
    
    return maxsum_global