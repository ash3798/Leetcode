def isSafe(row , col):
    if colArr[col] == 1 or rightDiag[row+col] == 1 or leftDiag[row-col+n-1] == 1:
        return False
    return True
    
def SolveNQueens(row):
    if row == n :
        print("completed path")
        return 1
    
    count = 0
    for col in range(n):
        if isSafe(row , col) :
            colArr[col] = 1
            rightDiag[row+col] = 1
            leftDiag[row-col+n-1] = 1
            
            count += SolveNQueens(row+1)
        
            colArr[col] = 0
            rightDiag[row+col] = 0
            leftDiag[row-col+n-1] = 0
    
    return count
    
n = 4

colArr = [0] * n
rightDiag = [0] * (2*n -1)
leftDiag = [0] * (2*n -1)
print(SolveNQueens(0))