# -*- coding: utf-8 -*-
"""
Created on Sun Mar 14 19:06:30 2021

@author: ashis
"""
# A utility function to print grid
def printing(arr):
    for i in range(9):
        for j in range(9):
            print(arr[i][j], end = " ")
        print()
        
def isValid(grid , cr , cc , num):
    #row check
    for i in range(9):
        if grid[i][cc] == num:
            return False
    #col check
    for j in range(9):
        if grid[cr][j] == num:
            return False
    #block check
    blockstartrowind = cr - cr%3
    blockstartcolind = cc - cc%3
    for i in range(3):
        for j in range(3):
            if grid[blockstartrowind+ i][blockstartcolind+ j] == num :
                return False
    return True


def solveSudoku(grid , sr , sc):
    print("sr :", sr , "  sc :" , sc)
    if sr==8 and sc == 9 :
        return True
    
    #adjust the coloumns and rows once one whole row gets processed
    if sc == 9:  
        sc = 0
        sr += 1
        
    if grid[sr][sc] != 0:
        return solveSudoku(grid , sr , sc+1)
    
    for num in range(1,10):
        if isValid(grid , sr , sc , num) == True:
            grid[sr][sc] = num
            if solveSudoku(grid , sr , sc+1) == True:
                print("returning true")
                return True
        
        grid[sr][sc] = 0
    
    return False


grid = [[3, 0, 6, 5, 0, 8, 4, 0, 0],
        [5, 2, 0, 0, 0, 0, 0, 0, 0],
        [0, 8, 7, 0, 0, 0, 0, 3, 1],
        [0, 0, 3, 0, 1, 0, 0, 8, 0],
        [9, 0, 0, 8, 6, 3, 0, 0, 5],
        [0, 5, 0, 0, 9, 0, 6, 0, 0],
        [1, 3, 0, 0, 0, 0, 2, 5, 0],
        [0, 0, 0, 0, 0, 0, 0, 7, 4],
        [0, 0, 5, 2, 0, 6, 3, 0, 0]]
 
if solveSudoku(grid , 0 , 0) == False:
    print("no solution")
else:
    printing(grid)
