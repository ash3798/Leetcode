#happy numbers are the one where we add the square of each digits and resulting number comes out to be 1 . if it dont we keep doing this untill it becomes 1.
#Non happy number will keep iterating in loop infinitely


#here we will try to exploit the fact that the number is not happy if it reaches a already seen number again during iterations.


#approach 1  : use array to store already seen nums            Complexity=  space:O(n)
#we keep iterating till we find that sum of square of digits as 1
#also we will keep track of the nums already encountered
#every time we get new num , we see if we have already seen it or not 
#if yes then , it not a happy number

def HappyNumber(num) :
    def sumOfSquareOfDigits(num) :
        sum = 0
        while num >0 :
            digit = num%10
            sum += digit*digit
            sum /= 10
        return sum

    alreadySeen = dict()      #to keep track of num encountered
    while True :            #run loop continuously till it breaches one of condition
        if num == 1 :
            return True

        if num in alreadySeen :
            return False
        
        alreadySeen[num] = 1
        num = sumOfSquareOfDigits(num)



#approach 2  : optimize space in approach 1
#the non happy numbers will create a cycle just like cycle in linked list 
#we can take two pointer one fast and one slow , fast will take two steps at a time ,slow will take one step at a time 
#two things can happen :
#   computed sum of squares of digit can become 1    =>  its a happy number
#   slow and fast pointers will become equal at some point  => it not happy number 



#approach 3 : use of the two single digit happy number (1, 7)
#we keep on computing the sumofsquaresofdigits  till we get a number that is single digit
#if that single digit is either 1 or 7 => its happy number 
#if its something else => not happy number