#corner cases :    {]}   , {}{  , ""

#approach 1 :Stack                Complexity : time:O(n)    space:O(n)
#we will use stack to accomplish the recursive structure of valid parenthesis problem
#we will keep mapping of various parenthesis (closing and opening counterparts) in map
#push if starting brace and pop from stack if closing brace is encountered
#finally in the end check if stack is empty or not

def ValidParenthesis(s) :
    stack = []

    mappings = { '}':'{' , ']':'[' , ')':'(' }

    for ch in s :
        if ch in mappings :
            if len(stack) != 0 :            #can't pop if len of stack is zero . this will mean closing brace do not have the opening brace in s
                popped = stack.pop()
                if popped != mappings[ch] :   #check if popped element matches the ending brace counterpart in mapping 
                    return False
            else :
                return False
        else :
            stack.append(ch)

    if len(stack) == 0 :
        return True
    return False

#driver code 
s = "()()([{])"
print(ValidParenthesis(s))