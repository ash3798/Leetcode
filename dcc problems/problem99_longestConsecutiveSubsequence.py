#longest Consecutive subsequence 
#eg :  [10,2,3,7,4,1,20]  , answer = 4  (ie. 1,2,3,4)


#approach 1 : Naive solution (Sorting)
#complexity :   time:O(nlogn)    |  space : O(1)
#   sort the array , and then iterate over it to see biggest consecutive sequence length you can find



#approach 2 : Hashing 
#complexity :  time:O(n)   |  space : O(n)
#   - we store all the elements to hashmap
#   - we can iterate over array to take each element as a potential start point , and try to see if next consecutive elements are there in map or not
#       -   if they are there , keep searching for next ones and increment counter
#       -   else skip to next element
#   Optimization :
#       - if element-1 is already there in map , we can ignore this element as its gonna get covered when element-1 is taken as start point



#approach 3 : Priority queue or Heap 
#complexity :  time:O(n)   |  space : O(n)
#   - put all elements to heap (min heap)
#   - we will extract elements and see if the (previous - current)== 1 ,  if yes this is consecutive and we incerment counter
#       - if no then this is start for new sequence
#   - in the end return the biggest length found


def findLongestConseqSubseq(nums) :
    if len(nums) == 0 :
        return 0

    heap = Heap()
    #push all elements to heap
    for num in nums :
        heap.insert(num)

    res = 0
    prev = 0    #if the range is just non negetive , otherwise put -2^31

    ctr = 0
    for i in range(len(nums)) :
        curr = heap.ExtractMin()

        if curr-prev == 1 :
            ctr += 1
            prev = curr
        elif curr-prev == 0 :
            prev = curr
        else:
            res = max(res , ctr)              #here streak is broken , so compare with res if bigger put it
            ctr = 1                         #since new sequence started here , reset the ctr
            prev = curr

    return res


#driver code 
nums=[10,2,3,7,4,1,5]
print(findLongestConseqSubseq(nums))


#heap class for reference
# class Heap :
#     def __init__(self):
#         self.val = []
        
#     def insert(self,data):
#        self.val.append(data)
#        if len(self.val)>1 :
#            self.bubbleup()
    
#     def bubbleup(self):
#         ci = len(self.val)-1
        
#         while ci > 0 :
#             pi = (ci-1)//2
            
#             if self.val[pi] > self.val[ci] :
#                 self.val[pi] , self.val[ci] = self.val[ci],self.val[pi]
#                 ci = pi
#             else:
#                 break
    
#     def ExtractMin(self):
#         if len(self.val) ==0:
#             return "no enteries till now "
        
#         min = self.val[0]
#         self.val[0] = self.val[len(self.val)-1]
#         self.val = self.val[:len(self.val)-1]
#         self.sinkDown()
#         return min
    
#     def sinkDown(self):
#         if len(self.val) == 0:
#             return 
        
#         ci= 0
        
#         while ci < len(self.val):
#             isSwapped = False
#             min = ci
#             lc = 2*ci+1
#             if lc < len(self.val) and self.val[lc] < self.val[min] :
#                 min = lc
#                 isSwapped = True
            
#             rc = 2*ci+2
#             if rc < len(self.val) and self.val[rc] < self.val[min] :
#                 min = rc
#                 isSwapped = True
            
#             if isSwapped == True :
#                 self.val[min] , self.val[ci] =  self.val[ci] , self.val[min]
#                 ci = min
#             else :
#                 break