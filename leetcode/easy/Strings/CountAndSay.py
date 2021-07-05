def CountAndSay(s) :
    ctr = 0
    res = ""
    current = s[0]
    
    for i in range(len(s)):
        if s[i]== current:
            ctr += 1
        else:
            res = res + str(ctr) + str(current)
            current = s[i]
            ctr = 1
    
    res = res + str(ctr) + str(current)
    return res

def nthcountandsay(n) :
    if n == 1 :
        return "1"

    return CountAndSay(str(nthcountandsay(n-1)))  #convert to string before passing it to countandsay

#driver code
n = 3
print(nthcountandsay(n))    