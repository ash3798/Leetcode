#merge sort
#   split array from mid
#   sort both left and right recursively
#   merge both the sorted left and right into single sorted array

def mergeSort(arr) :
    if len(arr) > 1 :
        n = len(arr)

        mid = n//2

        left = arr[:mid]
        right = arr[mid:]

        mergeSort(left)
        mergeSort(right)

        i = 0
        j = 0
        k = 0

        while i < len(left) and j < len(right) :
            if left[i] <= right[j] :
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            
            k += 1
        
        while i < len(left) :
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right) :
            arr[k] = right[j]
            j += 1
            k += 1

        
#caller code
arr = [38,27,43,300,9,82,10]
mergeSort(arr)
print(arr)