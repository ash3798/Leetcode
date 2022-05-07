def getMinMax( a, n):
    max = -2**31
    min = 2**31-1
    
    for num in a:
        if num > max :
            max = num
        
        if num < min :
            min = num
    
    return [max ,  min]