#approaches 

#approach 1 : Naive approach       Complexity : time:O(n)    space:O(1)
#we are checking for all the divisors in each number using if else ladder and returning the resulting value
#shortcoming : this code will become too long and hard to mantain if we take many divisors


#approach 2 : String concatination (improvement to naive approach)    Complexity : time:O(n)    space:O(1)
#instead of taking too many pricise if conditions , we will use string concat which inturn will decrease number of conditions required 
#we will begin with empty string , and concat the appropriate string if we n is divisible by some divisor


#approach 3 : hashing       Complexity : time:O(n)    space:O(1)  , ideally space should be O(m) and time should be O(n*m), but since no of divisors are gonna be some even if n = 1000 or 1 million
# (for very large numbers of divisors  , above two will become hard to mantain (for addition and removal also ))
#we can now store our divisors into a ordered dictionary or array , since we dont need lookup  instead we need to access all in order


# #approach 1 :
# def fizzBuzz(n: int) :
#     result = [None]*n
#     for i in range(0,n):
#         if (i+1)%3 == 0 and (i+1)%5 == 0 :
#             result[i]= "FizzBuzz"
#         elif (i+1)%3 == 0 :
#             result[i]= "Fizz"
#         elif (i+1)%5 == 0 :
#             result[i]= "Buzz"
#         else :
#             result[i]= str(i+1)
    
#     return result

################################################

# #approach 2 :
# def fizzbizz(n):
#     result = []

#     for i in range(1,n+1):
#         temp = ""

#         if i % 3 == 0:
#             temp += "fizz"
#         if i%5 ==0 :
#             temp += "buzz"

#         if temp == "" :
#             temp += str(i)
        
#         result.append(temp)
    
#     return result

##################################################
#approach 3 :
def fizzbizz(n):
    result = []

    #dict to store all fizzbuzz mappings , Note : order should be mantained while accessing keys
    dict = {3: "fizz" , 5 : "buzz"}

    for i in range(1, n+1):
        temp = ""

        for key in dict.keys():
            if i%key == 0 :
                temp += dict[key]

        if temp == "" :
            temp += str(i)

        result.append(temp)
    
    return result