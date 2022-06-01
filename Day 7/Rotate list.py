#In this question we are asked to rotate the given linked list by k.

#Brute force approach:
#In this approach for k times we move the last node to first node

# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if head == None or head.next == None:
            return head
        
        temp = head
        for i in range(k):
            temp = head
            while temp.next.next!=None:
                temp = temp.next
            end = temp.next
            temp.next = None
            end.next = head
            head = end
        
        return head
    
    #Time Complexiy: O(n*k)
    #Space Complexity: O(1)
    
    
#Optimized approach:
#In this approach we make the list cyclic by moving to end and setting its next to head, then from head we traverse k%length and then disjoint the cycle

     def rotateRight(self, head, k):
        if head == None or head.next == None or k == 0:
            return head
        length = 1
        temp = head
        while temp.next!=None:
            length+=1
            temp = temp.next
        temp.next = head
        
        k = length-k%length
        
        for i in range(k):
            temp = temp.next
        head = temp.next
        temp.next = None
        
        return head
    
    #Time Complexity: O(n) + O(length-k%length)
    #Space Complextiy: O(1)
