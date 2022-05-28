#In this question we are asked to remove nth node from the end in a linked list.

#Naive approach:
#In this approach we first calculate the length of linked list and then remove the length-n element

# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        length = 0
        temp = head
        if head ==None:
            return None
        
        while temp:
            temp = temp.next
            n+=1
            
        if temp == None:
            head = head.next
            return head
            
        x = length - n
        
        temp = head 
        for i in range(x-1):
            temp = temp.next
            
        temp.next= temp.next.next
        
        return head
    
    #Time Complexity: O(2n)
    #Space Complexity: O(1)
    
    
    def removeNthFromEnd(self, head, n):
        herald = head
        follower = head
        
        head.next == None:
            return None
        
        for i in range(n):
            herald = herald.next
            
        if herald == None:
            head = head.next
            return head
        while herald.next!=None:
            follower = follower.next
            herald = herald.next
            
        follower.next = follower.next.next
            
        return head
        
    #Time Complexity: O(n)
    #Space Complexity: O(1)
            
