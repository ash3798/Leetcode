def getRange(num1, num2,res):
    if num1 == num2 :
        res.append(str(num1))
    else:
        res.append(str(num1) + "->" + str(num2))

def findMissingRanges(nums , lower , upper):
    #iterate array elements on by one , keep track of expected target
    #see if  exptarget < num[i]-1  => missing range
    #   if exptarget > num[i]-1  => no action needed , duplicate element in array
    #   if  exptarget == num[i]-1   => nothing missing
    #handle last element with upper limit seperately
    
    res = []
    expTarget = lower
    for i in range(len(nums)):
        if nums[i] == expTarget :
            expTarget += 1
            continue
        elif nums[i] < expTarget:
            continue
        else :
            getRange(expTarget , nums[i]-1 , res)
            expTarget = nums[i]+1
    
    if expTarget <= upper:
        getRange(expTarget , upper, res)

    return res

#driver code
nums = [3,50,75]
lower = 0 
upper = 99

print(findMissingRanges(nums , lower,upper))