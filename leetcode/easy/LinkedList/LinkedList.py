class ListNode:
    def __init__(self, value=0 , next=None):
        self.val = value
        self.next = None
    
class LinkedList:
    def __init__(self , val : int):
        self.head = ListNode(val)

    def printLinkedList(self , head: ListNode):
        curr = head 
        while curr :
            print(curr.val)
            curr= curr.next

    def deleteNode(self , node):  #given is the node which needs to be removed
        while node.next.next != None :
            node.val = node.next.val
            node = node.next

        node.val = node.next.val
        node.next = None

    #two approaches :
        #two pass approach :     time:O(n)     space:O(1)
            # perform one pass => find length of linked list . 
            # subtract the target from length and delete target-length node
        #one pass approach :     time:O(n)     space:O(1)
            #use two pointer , give one pointer headsup equal to target , one at beginning
            #start moving both these pointers forward 
            #when the fast pointer reaches the end , that means the slow one has reached the node to be deleted
            #delete that node.
            #Note : keep track of prev node along with current in order for deletion
    def removeNthNode(self, head :ListNode , n: int) :
        fast = head
        slow = head

        while fast.next != None and n > 1:   #add distance between the fast and slow , so that slow reaches the prev node of the node to be deleted
            fast = fast.next
            n -= 1
        
        prev = None
        while fast.next != None :
            prev = slow
            slow = slow.next
            fast = fast.next
        
        #delete the node on reaching prev node
        if prev == None :
            head = head.next
        else:
            prev.next = prev.next.next

        return head

    #iteratively :
        #we can keep track of nodes with 3 pointers => prev , curr , next  so that while switching links i wont lose track of any of the nodes
        #switch the node.next values accordingly for all nodes
    #recursively :
        #we need to recursively call for the reverse func for next node in line untill we hit base case i.e node.next=null
        #we need to keep track of what our head will be in reversed list 
        #so return value of function should be new head  and rest of the logic to switch the next pointers can be independent of it
    def reverseLinkedList(self, head) :
        def reverse(node):
            if node.next == None:
                return node

            newHead = reverse(node.next)
            #invert the next pointers
            tmp = node.next.next
            node.next.next = node
            node.next = tmp
            
            return newHead

        #call inline reverse func for head
        self.head = reverse(head)

    #we can create a sentinal(dummy) node first to keep track of the head and reduce the extra special handlings needed on head
    #we can have two pointer one at each list and then compare the values 
    # we will take node with smaller value and append it to final list and  move the ppointer of selected list forward 
    # keep repeating steps untill one of the list ends 
    # after that append all the elements of the remaining list  
    def mergeTwoSortedLinkedList(self , head1 , head2):
        l1 = head1
        l2 = head2
        res = ListNode()
        curr =res
        while l1 != None and l2 != None :
            if l1.val < l2.val :
                curr.next = ListNode(l1.val)
            else:
                curr.next = ListNode(l2.val)
            
            curr = curr.next
        
        while l1 != None :    #need to change code to add new nodes res each time we need to add value
            curr.next = l1
        
        while l2 != None :
            curr.next = l2

        return res.next

    #we will try the length of the linked list , for efficiency we will use false and slow pointer 
    #once fast pointer reaches end , out slow pointer reaches the mid 
    #we will reverse the linked list from mid to end  and get our new head for that reversed portion 
    #we will start a 2 pointer comparison on both the head of ll and the reversed portion to find if palindrome or not
    def isPalindrome(self , head):
        if head == None or head.next == None :
            return True

        fast = head 
        slow= head 

        while fast.next != None  and fast.next.next != None :
            fast= fast.next.next
            slow = slow.next

        def reverse(node):
            if node.next == None:
                return node

            newHead = reverse(node.next)
            #invert the next pointers
            tmp = node.next.next
            node.next.next = node
            node.next = tmp
            
            return newHead

        revcurr = reverse(slow.next)
        curr = head
        while(curr != None and revcurr != None):
            if curr.val != revcurr.val :
                return False
            curr= curr.next
            revcurr = revcurr.next
        return True

    #in order to detect cycle we will take two pointers :  one fast and one slow
    #now if linked list has no cycles then fast pointer can never meet the slow pointer 
    #but it meets or intersects somewhere , that means we have a cyle in linked list
    def hasCycle(self , head):
        if not head :
            return False
        
        fast = head 
        slow = head 

        while fast.next != None and fast.next.next != None :
            #first move them to next position then compare , otherwise both will be head in the beginning
            fast = fast.next.next
            slow = slow.next
            if fast == slow :
                return True
        
        return False


#driver code
ll = LinkedList(5)
ll.head.next = ListNode(10)
ll.printLinkedList(ll.head)
print("\n")
ll.reverseLinkedList(ll.head)
ll.printLinkedList(ll.head)
