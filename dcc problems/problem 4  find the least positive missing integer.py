# -*- coding: utf-8 -*-
"""
Created on Thu Feb 25 08:48:12 2021

@author: ashis
"""

def segregate(arr , size):
    j=0
    for i in range(size):
        if arr[i]<=0 :
            arr[j] , arr[i] = arr[i] , arr[j]
            j += 1

    return j

def findPositive(arr ,shift , size):
    for i in range(shift ,size):
        if abs(arr[i])-1+shift < size and abs(arr[i])-1+shift >= 0 + shift :
            arr[abs(arr[i])-1+shift] = -arr[abs(arr[i])-1+shift]
        
    for i in range(shift, size):
        if arr[i] > 0 :
            return i+1-shift
        
    return size+1-shift
    
def findMissing(arr , size):
    shift = segregate(arr ,size)
    
    return findPositive(arr, shift , size)

arr = [ 0, 10,1,3,5, 2,-10, -20 ]
print(findMissing(arr , len(arr)))