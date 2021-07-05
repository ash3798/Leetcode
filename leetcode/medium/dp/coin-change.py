def countCoins(memo ,coins , amt):
    if memo[amt] != -1 :
        return memo[amt]
    
    minVal = 2**31-1
    for i in range(len(coins)) :
        if amt >= coins[i] :
            amt -= coins[i]
            count = countCoins(memo , coins , amt)
            amt += coins[i]
            if count != -1 :
                minVal = min(minVal, count)
    
    if minVal != 2**31-1 :
        memo[amt] = minVal +1
    else :
        memo[amt] = -1

    return -1    

#driver function
coins = [1,3,5]
amount = 7

if amount == 0 :
    print(0)

memo = [-1]*(amount+1)
for val in coins :
    if val < amount :
        memo[val] = 1
memo[0] = 0

for i in range(amount+1):
    countCoins(memo ,coins , i)

print(memo)
print(memo[amount])  

#approach 1 brute force 
# def countCoins(coins , indCoin ,amt):
#     if amt == 0 :
#         return 0
    
#     if indCoin < len(coins) and amt > 0 :
#         maxVal = amt//coins[indCoin]
#         minCost = 2**31-1
        
#         for i in range(0 , maxVal+1) :
#             if amt >= i*coins[indCoin] :
#                 amt -= i*coins[indCoin]
#                 res = countCoins(coins , indCoin+1 , amt)
#                 amt += i*coins[indCoin]
#                 if res != -1 :
#                     minCost= min(res+i , minCost)
        
#         if minCost == 2**31-1 :
#             return -1
#         else :
#             return minCost
        
#     return -1


# #driver function
# coins = [1,2,5]
# amount = 100
# print(countCoins(coins , 0 , amount))