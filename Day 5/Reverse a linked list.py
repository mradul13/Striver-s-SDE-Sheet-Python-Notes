#In this question we are given a linked list and we simply have to reverse it.

#iterative approach:
#In this approach we will use three pointers and succesively reverse the direction of the nodes

# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        prev = None
        curr = head
        
        
        while curr != None:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
            
        return prev
    
    #Time Complexity: O(n)
    #Space Complexity: O(1)
