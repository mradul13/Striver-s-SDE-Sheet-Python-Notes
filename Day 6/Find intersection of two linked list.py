#In this question we are asked to find the intersection of two linked list.

#Brute Apporach:
#In this appraoch we basically check for every node, using two loops:

# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        temp1 = headA
        temp2 = headB
        while temp1!=None:
            while temp2!=None:
                if temp1==temp2:
                    return temp1
                temp2 = temp2.next
            temp1 = temp1.next
        return None
    
    #Time Complexity: O(n*m)
    #Space Complexity: O(1)
    
    
#Hashing:
#In this approach we first iterate through one list and store its nodes in hashmap, and then while iterating through second list check for intersection.

    def getIntersectionNode(self, headA, headB):
        hash = {}
        temp1 = headA
        temp2 = headB
        while temp1!=None:
            hashmap[temp1]=1
            temp1 = temp1.next
        while temp2!= None:
            if temp2 in hashmap:
                return temp2
            temp2 = temp2.next
        return None
    
    #Time Complexity: O(n+m)
    #Space Complexity: O(n or m)
    
    
#Length difference method:
#In this method we first find lengths of both lists and then find difference, and accordingly place the head of both lists such that both have same lengths
#Then iterate and try to find intersection

    def getIntersectionNode(self, headA, headB):
        temp1 = headA
        temp2 = headB
        len1 = 0
        len2 = 0
        
        while temp1!=None:
            len1+=1
            temp1 = temp1.next
        while temp2!= None:
            len2+=1
            temp2 = temp2.next
            
        diff = len1-len2
        
        if diff<0:
            for i in range(len2-len1):
                headB = headB.next
        else:
            for i in range(len1-len2):
                headA = headA.next
        
        while headA!=None:
            if headA == headB:
                return headA
            headA = headA.next
            headB = headB.next
            
        return headA
    
    #Time Complexity: O(n+m) + O(abs(len1-len2)) +O(min(l1,l2))
    #Space Complexity: O(1)
    
    
#Optimized approach:
#Using the same intuition as difference of length we can optimize our solution:

    def getIntersectionNode(self, headA, headB):
        temp1 = headA
        temp2 = headB
        while temp1!=temp2:
            if temp1 == None:
                temp1 = headB
            else:
                temp1 = temp1.next
            if temp2==None:
                temp2 = headA
            else:
                temp2 = temp2.next
        return temp1
    
    #Time Complexity: O(2n)
    #Space Complexity: O(1)
                
        
            
    
    
    
                
