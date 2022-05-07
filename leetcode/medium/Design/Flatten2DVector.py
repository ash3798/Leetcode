#MAin task here is to handle the corner scenarios and making sure that hasNext gives false if not element is there , and if hasNext() returns true then next() returns the appropriate next element
# handle scenarios of : column going out of range => move to next row and reset the col to zero
#                       rows getting out of bound => return false in hasNext()
#                       handle empty arrays => skip the rows with zero length

class vector2d:
    def __init__(self, vec):
        self.vec2d = vec
        self.currRow = 0
        self.currCol = 0
        self.numRows = len(self.vec2d)

    def next(self):
        ans = 0
        if self.currRow < self.numRows and self.currCol < len(self.vec2d[self.currRow]):
            ans = self.vec2d[self.currRow][self.currCol]

        self.currCol += 1
        if self.currCol >= len(self.vec2d[self.currRow]) :
            self.currCol = 0
            self.currRow += 1

        return ans

    def hasNext(self) :
        while self.currRow < self.numRows and len(self.vec2d[self.currRow]) == 0 :
            self.currRow += 1

        return self.currRow < self.numRows and len(self.vec2d[self.currRow])

#driver code
vect = [[1,2,3,4,5], [] ,[6,7,8],[] ,[9,10]]
vobj = vector2d(vect)

while vobj.hasNext() :
    print(vobj.next())