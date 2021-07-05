#corner case :  x=1   , x=0

#approach 1 : check all the integers till x to find the biggest number where (i*i < x)
#Complexity : time:O(sqrt(x))   | space: O(1)



#approach 2 : use binary search            Complexity : time:O(log(x))   | space: O(1)
#   we will try to find biggest integer for which i*i < x
#Note : take a variable ans where you store the num , for which you hit condition mid*mid < x
#       we keep overwriting it every time we hit , and return that as answer when limits pass each other

