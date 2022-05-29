#In this question, given a linked list we have to find whether it is cyclic or not

#Hashing approach:
#In this approach we store encountered nodes in a set and successively check whether the present node is in set or not, if yes list is cyclical.

# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        hashset = set()
        while head != None:
            if head in hashset:
                return True
            else:
                hashset.add(head)
        return False
    
    #Time Complexity: O(n)
    #Space Complexity: O(n)
    
   
#Hare and Turtle:
#In this approach we take two pointers one moves 2 steps and another moves 1 step, if fast one encounters None, then it is not a cyclical list, and if list is cyclical
#slow and fast pointers are bound to collide

    def hasCycle(self, head):
        if head == None:
            return False
        hare = head
        turtle - head
        while hare.next != None and hare.next.next != None:
            hare = hare.next.next
            turtle = turtle.next
            if hare == turtle:
                return True
        return False
    
    #Time Complexity: O(n)
    #Space Complexity: O(1)

      
