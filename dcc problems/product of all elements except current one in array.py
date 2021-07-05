# -*- coding: utf-8 -*-
"""
Created on Sat Feb 20 00:44:59 2021

@author: ashis
"""

num = [1,2,3,4,5]

prefix = [1]* len(num)
suffix = [1]*len(num)

'''extra space
for i in range(1, len(num)):
    prefix[i] = prefix[i-1]*num[i-1]
    
j = len(num)-2
while j>=0 :
    suffix[j] = suffix[j+1] * num[j+1]
    j -= 1
    
for i in range(len(num)):
    num[i] = prefix[i] * suffix[i]
'''
result = [1]*len(num)

temp = 1
for i in range(len(num)):
    result[i] = temp
    temp *= num[i]

temp = 1
j = len(num)-1
while j>=0 :
    result[j] *= temp
    temp *= num[j]
    j -= 1
    
print(result)