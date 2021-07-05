#check if the number is negetive
#just make it positive for time being and return with sign during sending res

#just start creating the reverse number one step at a time and also keep comparing to the limit along the way
#if it ever crosses limit just return 0  otherwise the number itself

def reverse(num) :
    res = 0
    while num>0 :
        res = res * 10 + (num%10)
        num = num//10

        if res > 2**31-1 :
            return 0
    return res

#driver code
num = 0

res = 0
if num < 0 :
    #pass it to function in the positive form itself and while returning append sign again
    res = -(reverse(-1*num))
else:
    res = reverse(num)

print(res)