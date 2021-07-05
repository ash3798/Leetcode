#complexity : time : O(nlogn) | space :O(2n)
def solve( A):
    if len(A) == 0 :
        return 0        
    
    st = []
    et = []
    
    for interval in A :
        st.append(interval[0])
        et.append(interval[1])
        
    st.sort()
    et.sort()

    print(st)
    print(et)

    sptr = 0
    eptr = 0
    
    while sptr < len(A):
        print(sptr, "   " , eptr)
        if st[sptr] >= et[eptr]:
            sptr += 1
            eptr += 1
        else :
            sptr += 1
            
    return sptr - eptr

#driver code 
A = [[7, 10],  [4, 19],  [19, 26],  [14, 16],  [13, 18],  [16, 21]]

print(solve(A))



# #complexity : time : O(n^2) | space :O(n)
# def solve( A):
#     if len(A) == 0 :
#         return 0
        
#     A = sorted(A , key = lambda x : x[0])
    
#     parallelMeetings = 0
#     endTimeRef = []
#     res = 0
#     for interval in A :
#         for i in range(len(endTimeRef)) :
#             if endTimeRef[i] != -1 and endTimeRef[i] <= interval[0] :
#                 parallelMeetings -= 1       #remove meetings from count that ended 
#                 endTimeRef[i] = -1
            
#         parallelMeetings += 1    #current meeting got started 
#         endTimeRef.append(interval[1])
#         res = max(res , parallelMeetings)

#     return res