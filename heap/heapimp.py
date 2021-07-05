# -*- coding: utf-8 -*-
"""
Created on Sun Mar  7 13:04:54 2021

@author: ashis
"""


class Heap :
    def __init__(self):
        self.val = []
        
    def insert(self,data):
       self.val.append(data)
       if len(self.val)>1 :
           self.bubbleup()
    
    def bubbleup(self):
        ci = len(self.val)-1
        
        while ci > 0 :
            pi = (ci-1)//2
            
            if self.val[pi] > self.val[ci] :
                self.val[pi] , self.val[ci] = self.val[ci],self.val[pi]
                ci = pi
            else:
                break
    
    def ExtractMin(self):
        if len(self.val) ==0:
            return "no enteries till now "
        
        min = self.val[0]
        self.val[0] = self.val[len(self.val)-1]
        self.val = self.val[:len(self.val)-1]
        self.sinkDown()
        return min
    
    def sinkDown(self):
        if len(self.val) == 0:
            return 
        
        ci= 0
        
        while ci < len(self.val):
            isSwapped = False
            min = ci
            lc = 2*ci+1
            if lc < len(self.val) and self.val[lc] < self.val[min] :
                min = lc
                isSwapped = True
            
            rc = 2*ci+2
            if rc < len(self.val) and self.val[rc] < self.val[min] :
                min = rc
                isSwapped = True
            
            if isSwapped == True :
                self.val[min] , self.val[ci] =  self.val[ci] , self.val[min]
                ci = min
            else :
                break
        
hp = Heap()
hp.insert(30)
hp.insert(20)
hp.insert(10)
hp.insert(50)
hp.insert(100)
print(hp.val)
hp.ExtractMin()
hp.insert(150)
hp.insert(90)
print(hp.val)
