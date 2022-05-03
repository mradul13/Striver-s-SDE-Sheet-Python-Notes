#In this question we are given an array of size n+1 in which numbers from 1 to n are resent. We have to find the number which appears more than one in the array.

#Using Sorting
#We can find the duplicate by sorting the array and then looping through elements finding if prev element is same as current.

class Solution(object):
    def findDuplicate(self, nums):
        nums.sort()
        i = 0
        while nums[i]!=nums[i+1]:
            i+=1
        return nums[i]
    
    #Time Complexity : O(nlogn +n)
    #Space Complexity : O(1)
    
    
    
    #Using Frequency Array:
    #In this approach we will use an frequency array to take counter of appearance of every number and if any number is more than one than its the duplicate
    def findDuplicate(self, nums):
        n = len(nums)
        freq = [0]*(n+1)
        for i in range(n):
            if freq[nums[i]]==0:
                freq[nums[i]]+=1
            else:
                return nums[i]
            
    #Time Complexity : O(n)
    #space Complexity : O(n)
    
    
    #Using linked list cycle:
    #In this method we wi;; use a linged list type logic by jumping to the index of the number we encounter starting from 0.
    #If there is duplicate a cycle will form inevitably.
    #We use two pinters fast and slow, fast moves by 2 and slow moves by 1. 
    #When the collide, we can say that the duplicate is equidistant from starting point and collision point.
    #so, we place fast pointer to starting point and now both point move by one, second collision is duplicate
    
    
    def findDuplicate(self, nums):
        fast = nums[0]
        slow = nums[0]
        
        while True:
            slow = nums[slow]        #One jump per loop
            fast = nums[nums[fast]]  #Two jumps per loop
            if fast == slow:
                break
        
        fast = nums[0]               #Fast set to starting point
        
        while fast!=slow:
            fast = nums[fast]
            slow = nums[slow]
    
        return slow
    
    #Time Complexity : O(n)
    #Space Complexity : O(1)
    
        
    
