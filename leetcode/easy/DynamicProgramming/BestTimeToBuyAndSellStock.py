#we need to earn max profit by buying and selling stock one time 

#approach : DP    time:O(n)   space:O(n)
#for getting maximum profit , we need to buy the stock at the lowest possible price and sell at highest
#   for this we need to go to each element and try to calculate profit using that element and minimum on left side of it
#   we will keep track of the minimum value to left for each index in lookup table instead of recalculating it again
#   along with this we will be keeping track of max profit , updating it if better profit is found 

# def maxProfit(prices):
#     minToLeft = [0]*len(prices)
#     minToLeft[0] = prices[0]
#     maxProfit = 0

#     for i in range(1,len(prices)):
#         maxProfit = max(maxProfit , prices[i]- minToLeft[i-1])

#         minToLeft[i] = min(minToLeft[i-1] , prices[i])
    
#     return maxProfit

# #driverCode
# prices= [7,1,5,3,6,4]
# print(maxProfit(prices))

#################################
#approach : Space optimizing above DP solution
#   since we are reffering to only on the element of minToLeft at a time , so we dont need to keep whole array , we can just use single variable

def maxProfit(prices):
    minToLeft = prices[0]
    maxProfit = 0

    for i in range(1,len(prices)):
        maxProfit = max(maxProfit , prices[i]- minToLeft)

        minToLeft = min(minToLeft, prices[i])
    
    return maxProfit

#driverCode
prices= [7,1,5,3,6,4]
print(maxProfit(prices))