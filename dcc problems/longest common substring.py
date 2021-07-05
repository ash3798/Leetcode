def longestCommonSubstring(s1 , s2) :
    len1 = len(s1)
    len2 = len(s2)
    
    dp = [[0 for k in range(len2+1)] for v in range(2)]    #since only two rows gets used at particular time in algo , so we optimized the space and used just two rows total and keep overwriting newest resutls in one andthen refer in other
    
    longestsslength = 0
    longestssendindex = 0
    
    for i in range(1, len1 +1):
        for j in range(1 , len2+1):
            if s1[i-1] == s2[j-1] :
                dp[i%2][j]  = dp[(i-1)%2][j-1] + 1
                if longestsslength < dp[i%2][j] :
                    longestsslength = dp[i%2][j]
                    longestssendindex = i-1
            else :
               dp[i%2][j] = 0 
    
    if longestsslength == 0 :
        return "no common substring"
    return s1[longestssendindex-longestsslength+1 : longestssendindex+1]
    
#driver program
s1 = "abcdef"
s2 = "kjuk"
lcs = longestCommonSubstring(s1, s2)

print(lcs)