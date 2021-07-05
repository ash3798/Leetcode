#class to represen single linked list node
class ListNode :
    def __init__(self , data):
        self.data = data
        self.next = None

def reverseLinkedList(node):
    if node.next == None :
        return node
    
    newHead = reverseLinkedList(node.next)
    temp = node.next.next
    node.next.next = node
    node.next =  temp
    
    return newHead

def reversePartially(head , start , end):
    curr = head 
    i =1
    
    while i < start-1 :
        curr = curr.next
        if curr == None:
            return "invalid indexes given"
        i += 1
   
    def rev(node , currIndex , target):
        if currIndex == target :
            return node
        
        newHead = rev(node.next , currIndex+1 , target)
        temp = node.next.next
        node.next.next = node
        node.next = temp
        
        return newHead
        
    curr.next = rev(curr.next , i+1 , end)
    
    return head
  
def middleOfLinkedList(head):
    fast = head 
    slow = head
    
    while fast.next != None and fast.next.next != None :
        fast = fast.next.next
        slow = slow.next
    
    print("middle of the linked list is :" , slow.data)
    return slow

def isPalindrome(head):
    if head == None  or head.next == None :
        return True
    
    mid = middleOfLinkedList(head)
    mid.next = reverseLinkedList(mid.next)
    
    p1 = head 
    p2 = mid.next
    
    while p2 :
        if p1.data != p2.data :
            return False
        p2 = p2.next
        p1 = p1.next
    
    return True

def deleteNode(head , target) :
    sen = ListNode(0)
    sen.next = head   #so that head need not be handled specially because it will also have a prev node now
    
    curr = head
    prev = sen
    
    while curr :
        if curr.data == target:
            prev.next = curr.next
            curr = curr.next
            continue
        
        prev = curr
        curr = curr.next
        
    return sen.next

def deleteNFromEnd(head , n):
    sen = ListNode(0)
    sen.next = head

    first = head
    while n > 0:
        first = first.next
        n -= 1
        
    second = sen
    while first != None:
        first= first.next
        second= second.next
    
    second.next = second.next.next
    return sen.next
    
def printLinkedList(head) : 
    curr = head
    while curr :
        print(curr.data)
        curr = curr.next
        
#driver program
head = None

head= ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(3)
head.next.next.next.next = ListNode(2)
head.next.next.next.next.next = ListNode(1)

#head = reverseLinkedList(head)

#head = reversePartially(head , 2 , 4)

#middleOfLinkedList(head)

#print(isPalindrome(head))
#head = deleteNode(head , 1)

head = deleteNFromEnd(head, 1)
printLinkedList(head)