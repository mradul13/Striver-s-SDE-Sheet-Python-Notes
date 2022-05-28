#In this question we have to delete the given node in constant time and instead of head node , the node to be deleted will be given.

#Approach:
#We will first set the data of the given node equals to data of node.next and then go on to delete the next node

# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val = node.next.val
        node.next = node.next.next
        
    #Time Complexity: O(1)
    #Space Comlexity: O(1)
