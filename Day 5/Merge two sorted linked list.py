#In this question, we are given two sorted linked list, we have to merge them.

#Approach 1:
#In this first approach, we will take another dummy linked list and link smallest node we find in two list and then go to next node in the list we find the smaller node

# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        dummy = ListNode()
        temp = dummy
        while list1 != None and list2 != None:
            if list1.val<list2.val:
                temp.next = list1
                temp = temp.next
                list1 = list1.next
            else:
                temp.next = list2
                temp = temp.next
                list2 = list2.next
            return dummy.next
    
    #Time Comlexity : O(n+m)
    #Space Complexity: O(n+m)
        
#Approach 2:
#In this approach, instead a taking a dummy array we will try to solve it in place
#First we take two pointers l1 and l2 and let l1 be the smaller one and then we run a loop and whenever we find that l1 is smaller than l2, we move l1 to next, 
#and store its current value in temp, if we find l2 smaller than l1 then we link temp to l2 and then swap l1 and l2

     def mergeTwoLists(self, list1, list2):
        
        if list1 == None:
            return list2
        if list2 == None:
            return list1
        if list1.val>list2.val:
            temp = list1
            list1 = list2
            list2 = temp
        
        res = list1
        
        while list1 != None and list2 != None:
            temp = None
            while list1.val<=list2.val and list1 != None:
                temp = list1
                list1 = list1.next
            temp.next = list2
            
            temp2 = list1
            list1 = list2
            list2 = temp
            
        return res
    
    #Time Complexity: O(n+m)
    #Space Complexity: O(1)
                
