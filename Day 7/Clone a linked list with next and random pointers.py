#In this question we are given a linked list with nodes having next and random pointers, we have to make an exact copy of the linked list

#Approach 1:
#In this approach we will use hashing to store hard copy of existing nodes and then use them to build the hard copy of the linked list

"""
# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        d = {}
        d[None] = None
        temp = head
        while temp:
            d[temp] = Node(temp.val)
            temp.next
        
        temp = head
        while temp:
            d[temp].next = d[temp.next]
            d[temp].random = d[temp.random]
            temp = temp.next
        
        return d[head]
    
    #Time Complexity: O(n)
    #Space Complexity: O(1)
    
#Approach 2:
#In this approach we will create nodes as we traverse through and then set random pointers in next traversal and then we will disjoint the new list.

    def copyRandomList(self, head):
        temp = head
        while temp:                                     #Add copy nodes of each original nodes next to them
            nex = temp.next
            temp.next = Node(temp.val)
            temp.next.next = next
            temp = temp.next.next
        
        temp = head
        while temp:
            if temp.random:
                temp.next.random = temp.random.next    #Now set random pointers for copy nodes on copy nodes
            temp = temp.next.next
        
        dummy = Node(0)
        out = dummy
        temp = head
        while temp:
            out.next = temp.next
            temp.next = temp.next.next                #Detach the two linked lists
            temp = temp.next
            out = out.next
        
        return dummy.next
            
    #Time Complexity: O(n)+O(n)+O(n)  approx O(n)
    #Space Complexity: O(1)
