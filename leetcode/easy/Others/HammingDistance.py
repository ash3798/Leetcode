#hamming distance between two numbers is the number of positions where the corresponding bits are different

#approach 1 :  inefficient
#we can calculate the hamming weight of num1 and num2 
#then we can do add of them , so that all the differing bits become zero 
#then again calculate the hamming weight of the result in prev step 
# then calculate the hamming distance by using (hw(num1) + hw(num2) - 2* hw(num1 & num2)) 



#approach 2 : optimal  (Using XOR)
#we can make use of XOR as it result in 1 on seeing different bits 
#we can do num1 ^ num2 , which will result in 1 being placed at all the positions where bits were different
#now we can find hamming weight of this result , which will be the hamming distance of num1 and num2
#more efficient as hamming weight need to be calculated only once


#approach 2:
def hammingdistance(num1 , num2):
    def hammingWeight(n) :
        oneBits = 0
        while n != 0 :
            n = n & (n-1) 
            oneBits += 1
        
        return oneBits
    
    diff = num1 ^ num2
    return hammingWeight(diff)

#driver code
num1 = 15
num2 = 8
print(hammingdistance(num1 , num2))