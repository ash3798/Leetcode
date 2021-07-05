#approaches 

#approach 1 :  use of loop or recursion       complexity : time:O(logb(n))    logb = log to base b   , b=3 here 
#   we take base value=1 , we keep on multiplying with 3 untill we get a number either equal to given number or greater than given number
#   if final value is == given , then yes its a power ,  otherwise its not
#Alternatively , we can keep dividing n , till we reach the 0 remainder

################################

#approach 2 : use the base conversion     Complexity : time:O(logb(n))
#   In Base 10, all powers of 10 start with the digit 1 and then are followed only by 0 (e.g. 10, 100, 1000). This is true for other bases and their respective powers.
#   same is the case with other bases , eg for base 2 , all the powers of 3 will be in form 10 , 100 , 1000 etc
#   
#therefore if we convert our number to base 3 and the representation is of the form 100...0, then the number is a power of 3.

# after converting , we can try to match it with regex which has pattern of (start with 1 and followed by all zero) 
#   ("^10*$")
#We will use the regular expression above for checking if the string starts with 1 ^1, is followed by zero or more 0s 0* and contains nothing else ＄.

###############################

#approach 3 : use of log          Time complexity : Unknown The expensive operation here is Math.log
#   i = log10(n) / log10(3)    , n is power of three only if i is an integer
#to check if i is integer ,  we need to do  i%1 == 0
#
#Common pitfalls 
#This solution is problematic because we start using doubles, which means we are subject to precision errors. 
# This means, we should never use == when comparing doubles. That is because the result of Math.log10(n) / Math.log10(3) could be 5.0000001 or 4.9999999.
# This effect can be observed by using the function Math.log() instead of Math.log10().
#In order to fix that, we need to compare the result against an epsilon.

#  return (Math.log(n) / Math.log(3) + epsilon) % 1 <= 2 * epsilon;

##############################

#approach 4 : Integer              complexity : time:O(1)
#we will make use of the fact that higher powers of number is divisible by lower powers of same number
#find out the value i such that its less than equal to the maxvalue of Integers allowed and it should be a power of 3
#now if  i % n == 0 , that means n is the power of 3 , else not a power of 3

#  return n > 0 && 1162261467 % n == 0;