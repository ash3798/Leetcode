#corner case 
#if n is zero ,  then 0 trailing zeros


#approach 1 :  calculate factorial and then count zeroes at end
#CON : since factorial numbers are so big they start to overflow even for small nums, so this approach is not good



#approach 2 : we will calculate the powers of 5 in n!
#we know pair of 5,2 in prime factors give us the trailing zeroes.
#so we should could how many such pairs are there ,  but since powers of 2 are always gonnabe bigger than power of 5
#so if we calculate just the power of 5  , it will give us the number of trailing zeros
#for this we can use the method below :
#   number of power of five in n! =    floor(n/5) + floor(n/25) + .............  ,  till (n > 5^i (i.e denominator))
#Complexity:  time=O(log5(n)) , as we are incremetally dividing by powers of 5 