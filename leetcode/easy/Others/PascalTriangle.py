#pascal triangle is a classic example of DP
#because here we use the results computed in previous row to create the results of current row

#approach 1:
#complexity : time :O(n^2)   space :O(n^2) , because we are storing data to array of array to return
#handle cases of numrows = 0 , return the empty result[]
#               numsrows = 1 , return [1]

def PascalTriangle(numrows) :
    triangle = []

    if numrows == 0 :
        return triangle

    i = 0
    for i in range(numrows) :
        row = [0]*(i+1)      # set first element of row as 1
        row[0] = 1
        row[i] = 1

        for j in range(1,i) :
            row[j] = triangle[i-1][j-1] + triangle[i-1][j]   #refer to previous row elements to get values

        triangle.append(row)
    
    return triangle

#driver code
numrows = 4
print(PascalTriangle(numrows))
