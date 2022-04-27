#In this question, interviewer asks you to find a subarray in the given array which has maximum sum.

#Naive approach:
#In this approach, we use three nested loops, two nested loops for generating every possible subarray and one loop for summing up the subarrays.

class Solution(object):
    def maxSubArray(self, nums):
        n = len(nums)
        max = 0
        for i in range(n):
            for j in range(i, n):
                sum = 0
                for k in range(i, j):
                    sum = sum + nums[k]
                if sum>max:
                    max = sum
        return max
    
    #Time Complexity : O(n**3)
    #Space Complexity : O(1)
    
    
    #Better approach:
    #Instead of using third nested loop to add the numbers in subarray, we can use add the numbers in second nested loop and compare it to max
    
    def maxSubArray(self, nums):
        n = len(nums)
        max = 0
        for i in range(n):
            curr_sum = 0
            for j in range(i, n):
                curr_sum = curr_sum + nums[j]
                if curr_sum > max:
                    max = curr_sum
        
        return max
    
    
    #Time Complexity : O(n**2)
    #Space  Compexity : O(1)
    
    
    #Kadane's Algorithm:
    #In this approach we will use Kadane's Algorithm which basically says that any running sum which is less than zero is not worthwhile to be running sum.
    #If running sum has value less than zero, leave that and again begin from zero.
    
    def maxSubArray(self, nums):
        n = len(nums)
        runn_sum = 0
        #set max to value of first element not zero because the given array can have max sum in negative
        max = nums[i]
        for i in range(n):
            runn_sum = runn_sum + nums[i]
            if runn_sum > max:
                max = runn_sum
            if runn_sum < 0:
                runn_sum = 0
        return max
    
    #Time Complexity = O(n)
    #Space Complexity = O(1)
    
