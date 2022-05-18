#In this question we are asked to find the element that occurs more than n//2 in the given array, this condition is always true

#Brute force approach:
#In this approach we will go through each element and then check if it appears more than majority 

class Solution(object):
    def majorityElement(self, nums):
        majmark = len(nums)//2
        for i in range(len(nums)):
            count = 0
            for j in range(len(nums):
                if nums[i]==nums[j]:
                	count+=1
				if count>majority:
                    return nums[i]
        
    #Time Complexity : O(n*n)
    #Space Complexity : O(1)
                           
#Better Approach:
#In this approach we will use a data struture to to store the count of eah element and simultaneously check if its more than majority
                           
    def majorityElement(self, nums):
        hash = {}
        n = len(nums)
        majmark = n//2
        for i in range(n):
            if nums[i] in hash:
                hash[nums[i]]+=1
            else:
                hash[nums[i]] = 1
            if hash[nums[i]]>majmark:
                return nums[i]
     
    #Time Complexity: O(n)
    #Space Complexity: O(n)
                           
                           
#Optimal Approach:
#Moore's Voting Algorithm:
#In this approach, we know than majority element occurs n/2+x while all other elements occur n/2-x, So we will traverse through array and we will increase the,
#the counter by 1 if we encounter same element else we decrease counter
                           
    def majorityElement(self, nums):
        element = 0
        count = 0
        for i in range(len(nums):
            if count==0:
                element = nums[i]
            if nums[i]==element:
                count+=1
            else:
                count-=1
        return element           
                           
   #Time Complexity : O(n)
   #Space Complexity : O(1)                   
