#inversion is present in array if  arr[i] > arr[j] given i < j

def merge(arr , left , right , mid) :
    inv = 0
    i =0
    j=0
    k =0
    while i< len(left) and j < len(right) :
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
            inv += mid-i
        k += 1
    
    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1
    
    while j < len(right) :
        arr[k] = right[j]
        j += 1
        k += 1

    # print("merge",inv)
    return inv

def mergeSort(arr) :
    if len(arr) > 1:
        inv = 0
        n = len(arr)

        mid = n//2
        left = arr[:mid]
        right = arr[mid:]
        
        inv += mergeSort(left)
        inv += mergeSort(right)

        inv += merge(arr , left , right , mid)

        # print("ms",inv)
        return inv
    
    return 0

def calculateInversion(arr):
    return mergeSort(arr)

#caller code
arr = [8,4,2,1]
print(calculateInversion(arr))