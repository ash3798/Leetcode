#Complexity : time:O(n*j)   space:O(n)
def strStr(haystack , needle):
    #if needle is empty , return 0
    if len(needle) == 0 :
        return 0
    
    #if len of needle should be less than haystack
    if len(needle) > len(haystack) :
        return -1
    
    i = 0
    j = 0

    while i<len(haystack) :
        if haystack[i] == needle[j] :  #if match found , try to keep matching further characters
            i += 1
            j += 1
        else :
            i -= j-1    #if mismatch , then revert i to the char next to where the previous match started , 
            j = 0       #if no match had happened , then j will be 0 anyways and i will get incremented (i-(0-1)) = i+1
        
        if j == len(needle) :
            return i-j
    
    return -1

#this above approach can be optimized by applying the knuth morris prat algorithm
#because then we wont have to go all the way back when some mismatch occures getting some portion matched