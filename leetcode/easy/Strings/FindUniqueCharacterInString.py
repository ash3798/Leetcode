def findUnique(s) :
    #iterate all elements and make entry in map , if some duplicate is encountered make its index in map as -1
    my_dict= {}
    for i in range(len(s)) :
        if s[i] in my_dict:
            my_dict[s[i]] = -1
        else:
            my_dict[s[i]] = i
    
    minIndex = 2**31-1     #iterate all the values in map , ignore -1 as it is for duplicates and see which index is smallest 
    for val in my_dict.values():
        if val != -1 :
            minIndex = min(minIndex , val)

    if minIndex == 2**31-1:  #means we did not find any index that has not duplicate
        return -1
    return minIndex

#driver code
s = "loveleetcode"
print(findUnique(s))