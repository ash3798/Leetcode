#approach 0 :  Modify the elements of the stack while inserting in order to keep track of min element
#time and space Complexity : O(1)
class Node :
    def __init__(self , val):
        self.data = val
        self.next = None

class MinStack:
    def __init__(self):
        self.top = None
        self.min = 0  #default value , will get overwritten on first write

    def getTop(self):
        if self.top == None :
            print("stack is empty")
            return
        else:
            return self.top.data

    def printStack(self) :
        curr = self.top
        print("START")
        while curr != None :
            print(str(curr.data))
            curr = curr.next
        print("END")

    def push(self , val) :
        if self.top == None :
            node = Node(val)
            self.top = node
            self.min = val
        else :
            if val >= self.min :
                node = Node(val)
                node.next = self.top
                self.top = node
            else :
                temp = 2*val - self.min
                self.min = val

                node = Node(temp)
                node.next = self.top
                self.top = node
    
    def pop(self) :
        if self.top == None :
            print("stack empty")
        else :
            temp = self.top 
            self.top = self.top.next

            if temp.data >= self.min :
                return temp.data
            else :
                currMin = self.min
                self.min = 2 * currMin - temp.data
                return currMin

    def getMin(self):
        if self.top == None :
            print("stack empty")
        return self.min

#driver code 
ms = MinStack()
ms.push(6)
ms.push(5)
ms.push(7)
ms.push(1)
ms.push(9)
ms.push(3)

ms.printStack()

print(ms.pop())

print(ms.getMin())

print(ms.pop())
print(ms.pop())

print(ms.getMin())

print(ms.pop())
print(ms.pop())
print(ms.getMin())


# #########################################################################
# #approach 1:  Use two stacks in order to keep track of the min element also in O(1) time
# #space complexity : O(n)
# class MinStack:
#     def __init__(self):
#         self.stack = []
#         self.min = []
#         self.stacklen = 0

#     def push(self ,val):
#         if self.stacklen == 0 :
#             self.min.append(val)
#         else :
#             currMin = self.getMin()
#             self.min.append(min(currMin , val))

#         self.stack.append(val)
#         self.stacklen += 1

#     def pop(self):
#         self.stack.pop()
#         self.min.pop()
#         self.stacklen -= 1    #decrease length on pop()

#     def top(self):
#         if self.stacklen == 0 :
#             return None
#         return self.stack[len(self.stack)-1]

#     def getMin(self) :
#         if self.stacklen ==0 :
#             return None
#         return self.min[self.stacklen-1]


# #driver code 
# ms = MinStack()
# ms.push(6)
# ms.push(5)
# ms.push(7)
# ms.push(1)
# ms.push(9)
# ms.push(3)

# print(ms.top())

# ms.pop()

# print(ms.top())

# print(ms.getMin())

# ms.pop()
# ms.pop()
# print(ms.top())
# print(ms.getMin())