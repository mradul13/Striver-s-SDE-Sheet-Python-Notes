#In this question, we are asked to return the middle of the linked list given, if linked list length is even then return decond middle element.

#Naive approach:
#In this approach we will traverse the whole linked list once and count its length and then traverse again for n//2+1 times and return the node.

'''
class node:
    def __init__(data):
        self.data = data
        self.next = None
'''
class Solution:
    #  Should return data of middle node. If linked list is empty, then  -1
    def findMid(self, head):
        n = 0
        temp = head
        while temp != None:
            temp = temp.next
            n+=1
        
        temp = head
        for i in range(n//2):
            temp = temp.next
        return temp.data
            
    #Time Complexity: O(n) + O(n/2)
    #Space Complexity: O(1)
    
    
#Optimal approach:
#In this approac we will take two pointers one moving forward 2steps at a time and another 1 step at a time, due to this whenever the fast one reaches end,
#it is safe to say the slow one must have reached the middle
        
    def findMid(self, head):
        hare = head
        turtle = head 
        if head ==None:
            return -1
        while hare.next != None:
            turtle = turtle.next
            hare = hare.next.next
            if hare == None:
                break
        return turtle.data
    
    #Time Complexity: O(n)
    #Space Complexity: O(1)
