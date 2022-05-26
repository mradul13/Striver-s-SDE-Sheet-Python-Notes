#In this question we are asked to return the length of longest consecutive subsequence in the given array.

#Brute force approach:
#In this approach we first sort the array and then using a loop find the consecutive sequence

class Solution(object):
    def longestConsecutive(self, nums):
        nums.sort()
        ans = 1
        prev = nums[0]
        curr = 1
        for i in range(1,len(nums)):
            
            if nums[i]==prev+1:
                curr+=1
            elif nums[i]!=prev+1:
                curr = 1
            prev = nums[i]
            
            ans = max(ans,curr)
        
        return ans
    
    
    #Time Complexity : O(nlogn)
    #Space Complexity : O(1)  Ignoring stack space for sorting operation
    
    
#Optimal approach:
#In this approach we will store all elements in a hashtable and then through it to find longest sequence

    def longestConsecutive(self, nums):
        hash = {}
        for i in range(n):
            hash[nums[i]]=i
            
        ans = 1 
 
        for i in range(n):
            if nums[i]-1 not in hash:
                j = nums[i]
                while j in hash:
                    j+=1
                ans = max(j-nums[i], ans)
        return ans
    
    
    #Time Complexity: O(n)    as we go through each sequence only once
    #Space Complexity : O(n)
                
            
            
