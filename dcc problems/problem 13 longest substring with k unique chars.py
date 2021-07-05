# -*- coding: utf-8 -*-
"""
Created on Sat Mar  6 22:37:23 2021

@author: ashis
"""


def findLongestSubstring (str , k):
    dict = {}
    for i in range(97,27+97):
        dict[i]= 0
    
    maxLength= 0
    start = 0
    end = 0
    unique = 0
    while end < len(str) :
        if unique > k : #if unique characters move beyond range  start dropping from left
            temp = str[start]
            start += 1
            
            dict[ord(temp)] -= 1
            
            if dict[ord(temp)] == 0:
                unique -= 1
                end += 1
            continue
        
        if dict[ord(str[end])] > 0 :
            dict[ord(str[end])] = dict[ord(str[end])] + 1
        else :
            dict[ord(str[end])] = 1
            unique += 1
        
        if unique == k : #if unique chars are equal to req then calculate the length of substr and compare to max
            maxLength = max(maxLength , end-start+1)
            end += 1
        elif unique < k : # if unique chars are still less move forward to include more chars
            end += 1

    
    return maxLength

print(findLongestSubstring("abbaccd" , 2))