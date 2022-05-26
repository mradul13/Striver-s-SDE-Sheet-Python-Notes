#In this question we are asked, to return the length of longest subarray with sum of zero in an array containing both positive and negative numbers.

#Naive approach:
#In this approach we will generate all possible subarrayas and check thier sum and thier length

class Solution:
    def maxLen(self, n, arr):
        maxi = 0
        for i in range(n):
            sum = 0
            for j in range(i, n):
                sum+=arr[j]
            maxi = max(sum, maxi)
        return maxi
    
    
    #Time Complexity: O(n*n)
    #Space Complexity: O(1)
    
    
#Optimal approach:
#If we encounter same sum later in the array then the subarray between the index where we found that sum and to the current sum should be zero sum
#[1, 2, 3, -1, -2, -3 , -4 , -5] in this array we have 6 as sum at 2nd index and also at 5th index therefore subarray between 2nd and 5th has contributed zero to sum.

    def maxLen(self, n, arr):
        hash = {}
        maxi=0
        sum = 0
        for i in range(n):
            sum+=arr[i]
            if sum==0 and max==0:
                max=1
            if sum not in hash:
                hash[sum]=i
            if sum in hash:
                maxi = max(i-hash[sum], maxi)
            if sum==0:
                maxi = max(i+1, maxi)
                
        return maxi
    
    
#Time Complexity : O(n)
#Space Complexity ; O(n)
