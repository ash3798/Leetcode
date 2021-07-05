class MinStack:
    def __init__(self):
        self.stack = []
        self.min = []
        self.stacklen = 0

    def push(self ,val):
        if self.stacklen == 0 :
            self.min.append(val)
        else :
            currMin = self.getMin()
            self.min.append(min(currMin , val))

        self.stack.append(val)
        self.stacklen += 1

    def pop(self):
        self.stack.pop()
        self.min.pop()
        self.stacklen -= 1    #decrease length on pop()

    def top(self):
        if self.stacklen == 0 :
            return None
        return self.stack[len(self.stack)-1]

    def getMin(self) :
        if self.stacklen ==0 :
            return None
        return self.min[self.stacklen-1]


#driver code 
ms = MinStack()
ms.push(6)
ms.push(5)
ms.push(7)
ms.push(1)
ms.push(9)
ms.push(3)

print(ms.top())

ms.pop()

print(ms.top())

print(ms.getMin())

ms.pop()
ms.pop()
print(ms.top())
print(ms.getMin())