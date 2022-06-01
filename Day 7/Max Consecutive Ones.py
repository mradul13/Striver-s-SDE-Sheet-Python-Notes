#In this question we are given an array of 0s and 1s, and we are asked to return the maximum number of consecutive ones

#Approach:
#Approach is very simple, we traverse the array, if one is encountered, we increase the count and compare it to maxcount else we set count to 0

class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        maxcount = 0
        count = 0
        for i in range(n):
            if nums[i]==1:
                count+=1
                maxcount = max(maxcount, count)
            else:
                count = 0
        return maxcount
    
    
    #Time Complexity: O(n)
    #Space Complexity: O(1)
