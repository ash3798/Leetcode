#optimized peak valley   time : O(n)   space : O(1)
def calculateProfit(prices) :
    profit = 0
    for i in range(1,len(prices)):
        #if there is a peak in price , add that to our profit  else move on ahead
        if prices[i] > prices[i-1] :
            profit += prices[i]-prices[i-1]
    
    return profit

#driver code
prices=[7,6,4,3,1]
print(calculateProfit(prices))

#approach : peak valley   time : O(n)   space : O(1)
#we can try to find the valley first by comparing prices and moving forward
#after that try to find the peak that comes after valley 
#subtract them and then add to profit 
#keep repeating this until you reach end of array 