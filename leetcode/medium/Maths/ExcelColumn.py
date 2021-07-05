#corner case 
#coloumn name : A


#approach : tranform to number by using base conversion (base10 => base26)
#Complexity : O(n), ie length of string

# here we will follow the same rules as that of the decimal to binary conversion , but we will convert to base 26
# we will use formula 
#          (<base>^<correct index>) * <num rep of char>
#       eg:  
#        CDA =  (26^2 * 3)  +  (26^1 * 4)  +  (26^0 * 1)
