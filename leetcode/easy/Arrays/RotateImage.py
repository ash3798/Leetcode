def rotate (matrix):
    left = 0
    right = len(matrix)-1
    
    while left < right : #process all the concentric squares
        for i in range(right - left) : #iterate to process all elements of edge
            top = left   #its a square
            bottom = right #because its a square

            #these rules for rotating are going to stay same for each iteration 
            #added neccesary offset i at required indexes to make it work with all the elements of edge
            temp = matrix[top][left+i]
            
            matrix[top][left+i] = matrix[bottom-i][left]
            matrix[bottom-i][left] = matrix[bottom][right-i]
            matrix[bottom][right-i] = matrix[top+i][right]
            matrix[top+i][right] = temp

        left = left + 1
        right = right -1

#driver code
matrix = [[1,2],[3,4]]
rotate(matrix)
print(matrix)
