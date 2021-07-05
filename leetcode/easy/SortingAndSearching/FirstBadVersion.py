#approach :  use binary search to get the result on log time hence reducing the minimum number of calls

def firstBadVersion(n):
    good = 0
    bad = n

    while bad-good > 1 :
        mid = (good+bad)//2

        if isBadVersion(mid) :
            bad = mid
        else :
            good = mid

    return bad 

#created the dummy function same as given function in question
def isBadVersion(n) :
    global badstart
    if n>= badstart :
        return True
    return False


#driver code 
badstart =7

n= 10
print(firstBadVersion(n))