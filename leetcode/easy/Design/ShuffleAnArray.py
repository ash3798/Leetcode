#approaches

#approach 1 : making use of aux array     Complexity=  time:O(n^2)     space:O(n)
#make a copy of original array named aux
#we pick on random element from the aux => we will pop it off from aux and overwrite it in the original array
#popping off is done so that the each element has the same probability of getting selected


#approach 2 : Fisher yates Algorithm        Complexity=  time:O(n)      space:O(1)
#its the same idea as approach 1 but we are going to do it in place , to avoid the need of the extra time complexity of popping and space complexity of storing a copy
#we will make use of swapping here
#we will select a random element in array (0,n) => once selected we will swap it with the first element in array ,
#then select again from (1,n) => swap it with second element in array and so on.


#approach 1 :
# def shuffle(self):
#     aux = list(self.array)

#     for idx in range(len(self.array)):
#         remove_idx = random.randrange(len(aux))
#         self.array[idx] = aux.pop(remove_idx)

#     return self.array


#approach 2 :
import random
def shuffle(nums) :
    for i in range(0, len(nums)):
        indexToSwap = random.randrange(i , len(nums))
        #swap elements 
        nums[i] , nums[indexToSwap]  = nums[indexToSwap] , nums[i]

    return nums

#driver code 
nums = [1,2,3,4,5,6]
print(shuffle(nums))
