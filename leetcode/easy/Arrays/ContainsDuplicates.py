#approach : use of hashsets or use sets     time: O(n)   space: O(n)
#create set of the array and compare lengths of both
#we can hashsets to store values and to check whether we have encountered this value before .
def isDuplicatesPresent (nums) :
    my_dict = {}
    for num in nums:
        if num in my_dict :
            return True
        my_dict[num] = 1
        
    return False
#driver
nums= [1,2,3,4]
print(isDuplicatesPresent(nums))

#approach : sorting     time : O(n logn)     space : O(1)
# sort our array , once done all duplicates will come together 
# we can then parse array and see if  nums[i] is same as nums[i+1] 
# if yes : we have duplicates 


# brute force with O(n^2) complexity