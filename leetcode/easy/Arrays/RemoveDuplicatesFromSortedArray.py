def removeDuplicates(nums) :
    if len(nums) == 0 :
        return 0

    i = 0 
    j = i+1

    while j<len(nums) :
        #if mismatch is found , put it into its right place . if not move forward
        if nums[i] != nums[j] :
            i += 1
            nums[i] = nums[j]
        j += 1
    
    return i+1   #to make it in form or length not indexes

#drive code
nums = [0,0,1,1,1,2,2,3,3,4]
print(removeDuplicates(nums))
