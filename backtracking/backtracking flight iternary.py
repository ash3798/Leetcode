# -*- coding: utf-8 -*-
"""
Created on Sun Mar 14 18:06:47 2021

@author: ashis
"""
def createIternary(flightPairs , spoint , count):
    if count == len(flights):
        print("itr" ,iternary)
        return True
    
    for pair in flightPairs:
        if pair.source == spoint :
            if flights[pair.dest] == 0:
                iternary.append(pair.dest)
                flights[pair.dest] = 1
                if createIternary(flightPairs , pair.dest , count+1) == True:
                    return True
                else:
                    iternary.pop()
                    flights[pair.dest] = 0
        
    return False
            
     
class fpair:
  def __init__(self, src, dest):
    self.source = src
    self.dest = dest
    

#driver code    
startpoint = "akl"
flightPairs = [fpair("akl" , "ppl"),fpair("yul" , "hnl"),fpair("hnl" , "sfo"), fpair("hnl" , "akl"),fpair("yul" , "ord") , fpair("ord" , "sfo") , fpair("sfo" , "hnl")]
flights = {}
iternary = []

for pair in flightPairs:
    flights[pair.source] = 0
    flights[pair.dest] = 0
  
iternary.append(startpoint)
if createIternary(flightPairs , startpoint , 1) == False:
    print("no possible iternary")

    