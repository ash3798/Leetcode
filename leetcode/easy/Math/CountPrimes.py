#corner cases : numbers less that equal to 2

#approach 1 : dividing each number to see if prime or not
#to find out if each number is prime number we need to divide it with all the numbers less than it 
#if it divides then prime else not prime

#Optimizations:
# instead of dividing n with all numbers till n , we can just divide it with nums till sqrt(n)
#because number will not be divisible by any number after n/2 ,  also all the unique factors of n will already have gotten covered till sqrt(n) so we dont need to move any further

#complexity =>  time O(n^1.5)     space=O(1)


#approach 2 : The Sieve of Eratosthenes 
#complexity : time:O( n*log(log(n)) )           space : O(n)
#We start off with a table of n numbers. Let's look at the first number, 2. We know all multiples of 2 must not be primes, so we mark them off as non-primes. 
# Then we look at the next number, 3. Similarly, all multiples of 3 such as 3 × 2 = 6, 3 × 3 = 9, ... must not be primes, so we mark them off as well.
#  Now we look at the next number, 4, which was already marked off. So we will ignore that as multiple of 4 would have been marked off by 2 

#There is a slight optimization here, we do not need to start from 5 × 2 = 10.n fact, we can mark off multiples of 5 starting at 5 × 5 = 25, because 5 × 2 = 10 was already marked off by multiple of 2, similarly 5 × 3 = 15 was already marked off by multiple of 3.
#  Therefore, if the current number is p, we can always mark off multiples of p starting at p^2

#terminating loop condition can be p < √n, as all non-primes ≥ √n must have already been marked off. When the loop terminates, all the numbers in the table that are non-marked are prime.

#########################################

# #approach 1 :
# def CountPrimes(n):
#     count = 0
#     for i in range(2 , n+1):
#         if isPrime(i) == True :
#             print("num :" , i)
#             count += 1
#     return count

# def isPrime(num):
#     i = 2
#     while i*i < num :
#         if num % i == 0 :
#             return False
#         i += 1
#     return True

# #driver code 
# n = 100
# print(CountPrimes(n))


#############################################
#approach 2 :
def CountPrimes(n):
    if n <2 :
        return 0
    
    isPrime = [True]*(n)   #let all numbers are prime in beginning

    i =2
    while (i*i < n) :             #n is exclusive here acc. to question (should be clarified beforehand)
        if isPrime[i] != False:
            multiplier = 2                     
            while (i *multiplier < n ):           #mark off all the multiples of i except i itself
                isPrime[i*multiplier] = False
                multiplier += 1
        
        i += 1
    
    count = 0
    for i in range(2, n):         #count all the prime numbers 
        if isPrime[i] == True :
            count += 1
    
    return count

#driver code 
n = 3
print(CountPrimes(n))