#In this question we have to find the node where the loop starts in a linked list, if no loop is present return None

#Approach 1:
#In this approach we will use hash table to store already encountered nodes, and if the current node is found in hash table that is the starting point of the loop.

# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        hash = {}
        temp = head
        
        while temp!=None:
            if temp in hash:
                return temp
            else:
                hash[temp] = 1
        return None
    
    #Time Complexity: O(n)
    #Space Complexity: O(n)
    
    
#Approach 2: 
#In this approach we use two ponters one fast one slow and if they collide that means linked list has loop and after collision set slow to head and then both pointers,
#move one forward and next collision is the required node.


    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        hare = head
        turtle = head 
        while head != None and head.next != None:
            hare = hare.next.next
            turtle = turtle.next
            if hare == turtle:
                turtle = head
                while turtle != hare:
                    turtle = turtle.next
                    hare = hare.next
                return turtle
        return None
    
    #Time Complexity: O(n)
    #Space Complexity: O(1)
