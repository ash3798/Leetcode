#corner cases :  dividend is 0

#approch 1 : brute force                Complexity =  time:O(n) , n is quotient   |  space:O(1)
#here we will keep on adding the divisor to sum till we become greater than dividend 
#number of iterations it took , will be our quotient



#approach 2 : Bit manipulation          Complexity=  time:O(1) , only 32 iterations every time  | space:O(1)
#first try to find the most significant bit of the quotient
#   for that shift the divisor by i  ,  where i goes from 31 to 0
#   for i where we find that divisor is less or equal to dividend after shifting , we set bit at that i in our quotient
#       quotient |= (1 << i)
#   use temp var to keep track of the shifts that satisfied the condition
#   keep repeating these steps for 32 iterations