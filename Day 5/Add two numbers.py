#In this question, we are two lisked list representing two numbers in reverse order, we have to return a linked list that represents sum of these two given linked lists

#Approach:
#In this approach, we add numbers as in pen paper summation, we maintain a carry variable

# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
# carry = sum        self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummy = LisNode()
        temp = dummy 
        carry = 0
        while l1 != None or l2 != None or carry != 0:
            sum = 0
            if l1 != None:
                sum = sum + l1.val
                l1 = l1.next
            if l2 != None:
                sum = sum + l2.val
                l2 = l2.next
            sum = sum + carry
            carry = sum//10
            node = ListNode()
            node.val = sum%10
            temp.next - node
            temp = temp.next
        
        return dummy.next
    
    #Time Complexity: O(n+m)
    #Space Complexity: O(n+m)
