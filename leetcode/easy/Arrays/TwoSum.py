#approach : Use hash map      Complexity = time:O(n)     space:O(n)
def IsSumPresent(nums , target) :
    my_dict = {}

    #iterate array  but not fill hashmap in one go (so that duplicates can be handled)
    #for each element see if hashmap has the sum-element in it
    #if yes , then sum is present 
    #if no , then add the current element to hashmap and move on
    for i in range(len(nums)):
        complement = target-nums[i]
        if complement in my_dict :
            return [my_dict[complement] , i]
        else:
            my_dict[nums[i]] = i
    
#driver code 
nums = [3,3,2,4]
target = 6
print(IsSumPresent(nums , target))
