def convert(s):
    refMap = {"I":1 , "V":5, "X" :10, "L":50 , "C" :100 , "D":500, "M":1000}

    result = 0

    prev=0
    curr= 0
    i = len(s)-1
    while i >= 0 :
        curr = refMap[s[i]]
        
        if prev > curr :         #if previous seen element is bigger , this one should be subtracted from total
            curr = -1*curr
        
        result += curr

        prev = refMap[s[i]]
        i -= 1
    
    return result

#driver code 
s = "III"
print(convert(s))