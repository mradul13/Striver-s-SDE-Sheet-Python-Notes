#In this question we are given a linked list in which each node has an linked list of itself.
#All the lists are sorted and we have to return a normal linked list that too in sorted in order.

#Approach:
#We already know to merge two sorted linked lists, so we use that and recursion and reach to the last of the linked list and then merge the lists from there

'''

class Node:
    def __init__(self, d):
        self.data=d
        self.next=None
        self.bottom=None
        
'''

def flatten(root):
    def merge(l1, l2):
        res = Node(0)
        temp = res
        while l1 != None and l2 != None:
            if l1.data<l2.data:
                temp.bottom = l1
                temp = temp.bottom
                l1 = l1.bottom
            else:
                temp.bottom = l2
                temp = temp.bottom
                l2= l2.bottom
            if l1 != None:
                temp.bottom = l1
            else:
                temp.bottom = l2
                
        return res.bottom
    
    if root == None and root.next == None:
        return root
    
    root.next = flatten(root.next)
    
    root = merge(root, root.next)
    
    return root
    
    
    #Time Complexity: O(n)
    #Space complexity: O(1)
