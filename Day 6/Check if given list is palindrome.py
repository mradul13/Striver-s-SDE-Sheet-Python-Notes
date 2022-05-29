#In this question we are asked to check whether the given linked list is palindromic or not.

#Approach 1:
#In this approach we simply copy all node data to an array, and simply check if the array is palindromic or not.

# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        arr = []
        while head!=None:
            arr.append(head.val)
            head = head.next
        
        i = 0
        n = len(arr)=1
        
        while i<n:
            if arr[i]!=arr[n]:
                return false
            
            i+=1
            n-=1
        return True
    
    #Time Complexity: O(n)
    #Space Complexity: O(n)
    
    
#Approach 2:
#In this approach we find the node just behind the middle node and link it to reverse of rest of linked list amd then we check until None is reached.

    def isPalindrome(self, head):
        def reverse(head):
            prev = None
            curr = head
            while curr != None:
                next = curr.next
                curr.next = prev
                prev = cirr
                curr = next
            return prev
        
        def findMiddle(head):       #This function actually returns node previous to middle node
            hare = head
            turtle = head
            while hare.next != None and hare.next.next != None:
                hare = hare.next.next
                turtle = turtle.next
            return turtle
        
        m= findMiddle(head)
        m.next = reverse(m.next)
        n = m.next
        
        while n != None:
            if m.val != n.val:
                return False
            m = m.next
            n = n.next
            
        return True
    
    #Time Complexity: O(n) + O(n/2) + O(n/2)
    #Space Complexity: O(1)
