#In this question we are given a linked list and we have to reverse it in groups of k, the remaining portion must be left unreversed

#Approach:
#We will first calculate length
#then we will run a loop till length is greater than k, and substract at the end of each iteration
#Within it we will run a for loop for k-1 and in this loop we succesively bring next element of the first to the first index and push the original 
#first node one rank down

# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if head==None or head.next==None or k==1:
            return head
        
        length = 0
        temp = head
        while temp:
            length+=1
            temp = temp.next
        
        dummy = ListNode(0)
        dummy.next = head
        prev = curr = next = dummy
        
        while length>=k:
            curr = prev.next
            next = curr.next
            for i in range(1, k):
                curr.next = next.next
                next.next = prev.next
                prev.next = next
                next = curr.next
            prev = curr
            length-=k
        
        return dummy.next
    
    #Time complexity: O(n) + O(n)
    #Space complexity: O(1)
