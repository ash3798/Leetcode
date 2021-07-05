#we can use regex to satisfy the pattern mentioned in question
#remoce all the trailing and leading white spaces

# ('^[\+\-]?\d+') 
# here :  ^ tells that pattern should be at the start of line ( if it appears inside [^] then it means not(!) )
#         ? denotes once or none
#         \d  denotes digits

#we can try to find above regex to check if valid pattern present or not 

#now to bring the answer inside limits provided :   -2^31  and  2^31-1
#to bring inside upper limit , we can take min of (number , 2^31-1)
#to bring inside lower limit , we take max of (number , -2^31) 