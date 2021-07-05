def TowerOfHanoi(n , A , B ,C):
    if n != 0 :
        TowerOfHanoi(n-1 , A , C , B)
        print("Move disk from ", A , "to ", C)
        TowerOfHanoi(n-1 , B , A , C)

    return 

#driver code 

TowerOfHanoi(3 , "A" , "B" , "C")