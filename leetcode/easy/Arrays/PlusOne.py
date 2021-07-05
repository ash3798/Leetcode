def PlusOne(digits) :
    #start iterating from end
    #add one to the last digit , if carry comes move to next digit and add it 
    #keep repeating this process untill no carry comes
    carry = 1

    for i in range(len(digits)-1 , -1 , -1):
        sum = digits[i] + carry
        digits[i] = sum %10
        carry = sum//10

        if carry == 0 :
            return digits
    
    if carry != 0 :
        digits.insert(0 , carry)
    
    return digits

#driver code
digits = [9,9,9]
print(PlusOne(digits))
