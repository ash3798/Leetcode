def minPalPartition(s):
    n = len(s)

    palTable = [[False for i in range(n)] for j in range(n)]

    #put all 1 length palindromes as True
    for i in range(n):
        palTable[i][i] = True

    #find all palindromes of length 2 and above
    for i in range(2 , n):
        for j in range(0 , n-i):
            if i ==2 :
                if s[j] == s[j+i-1]:
                    palTable[j][j+i-1] = True          
            else :
                if s[j] == s[j+i-1] and palTable[j+1][j+i-2] :
                    palTable[j][j+i-1] = True
                
    c = [0] * n         #c contains the min number of cuts needed

    for i in range(n):
        if palTable[0][i] :
            c[i] = 0
        else :
            c[i] = 2**31-1
            for j in range(0 , i):
                if palTable[j+1][i] == True and 1 + c[j] < c[i] :
                    c[i] = 1 + c[j]

                print("c",c)

    print(c)
    return c[n-1]

#caller code
s = "abcdefghijkl"
print(minPalPartition(s))