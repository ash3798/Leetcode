#Check if a key is present in every segment of size k in an array
#k = segment size , t = target

#traverse whole array , but one segment at a time . check if we found target in that segment . keep repeating
#last segment needs to be handled explicitly , as it might be of size k or smaller
def checkKey(arr , t , k):
    n = len(arr)

    i = 0
    while i+k <n :
        j =0
        found = False
        while j < k :
            if arr[i+j] == t :
                found = True
                break
            j += 1
        
        if found == False:
            return "NO"

        i = i+k

    rem = n-i-1
    if rem == 0:        #length of array was mutiple of k ,all full sized segments
        return "YES"

    while rem < n:
        if arr[rem] == t:
            return "YES"
        rem += 1
    
    return "NO"

#drive code 
arr = [3, 5, 2, 4, 9, 3, 1, 7, 3, 11, 12, 3]
t =3
k=3
print(checkKey(arr , t ,k))

arr = [5, 8, 7, 12, 14, 3, 9]
t =8
k=2
print(checkKey(arr , t ,k))

arr= [21, 23, 56, 65, 34, 54, 76, 32, 23, 45, 21, 23, 25]
t =23
k=5
print(checkKey(arr , t ,k))