#approach :    complexity :  time:O(n) , space:O(n^2)
#visit all the indexes and check for the duplicates voilating board .
#done with single loop going over all the array checking for row , col , blocks
def isValid(board) :
    row_dict = set()
    col_dict = set()
    block_dict = set()

    #iterate through each element of the board and make corresponding entries to dicts
    #check for each element if it is getting duplicated in the row , block , col they are present in
    for i in range(9) :
        for j in range(9) :
            if board[i][j] == "." :
                continue
            #check for duplications in corresponding enteries in dicts
            currNum = board[i][j]  
            blockIndex = i//3*3 + j//3
            if (i,currNum) in row_dict or (j,currNum) in col_dict or (blockIndex,currNum) in block_dict :
                return False

            #if not duplicates found , then add corresponding entries to maps
            row_dict.add((i , board[i][j]))
            col_dict.add((j , board[i][j]))
            block_dict.add((blockIndex , board[i][j]))
    
    return True

#driver code
#board = [[0 for y in range(9)] for x in range(9)]
board = [["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
print(isValid(board))


#approach 2 : same as  above but we can use seperate loops for cols , rows and blocks
# to optimize space we can clean up the array after completing each row/col and again reuse the space for next row/col
