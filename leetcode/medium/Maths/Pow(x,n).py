#Notes :
#power could be -ve too , need to handle for that also


#approach 1 :  Brute force             Complexity :  time:O(n) , n= power  |  space:O(1)
#   in this we will multiply our number <power> times one by one in loop
#this will end up having time limit exceeded 


#approach 2 : divide and conquer with reusing calculated vals
#Complexity :  time:O(log(n))   ,  space:(1)
#   we will divide the power in 2 , and recusively keep dividing it
#   find the value for the first halve and reuse it instead of calculating again for second half
#   eg  5^10  = ( 5^5 * 5^5 )
#
# base case : num^0 = 1
# Note : since we are dividing ,we need to check odd and even als0 ,
#        as in odd will have to add one power extra after calculating half power
#
# For negetive : two alternative : 1) calculate by +ve and divide by 1 in final result
#                                  2) mutiply with 1/x  in odd case instead of x  