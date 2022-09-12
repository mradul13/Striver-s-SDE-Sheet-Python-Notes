#In this question, we are given an array and we have to return all the unique quadruplets having the given sum.

#Approach 1:
#In this approach we will use a hashset to remove duplicates and first sorting the array and then using three loops and binary search the remaining array

class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = set()
        n = len(nums)
        for i in range(n-3):
            for j in range(i+1, n-2):
                for k in range(j+1, n-1):
                    if target - nums[i]-nums[j]-nums[k] in nums[k+1:]:
                        temp = [nums[i], nums[j], nums[k], target-nums[i]-nums[j]-nums[k]]
                        res.add(tuple(temp))
        res = list(res)
        for i in range(len(res)):
            res[i] = list(res[i])
        return res
    
    #Time Complexity: O(n**3logn)+O(nlogn)
    #Space Complexity: O(m) m= number of quadruplets
    
    
#Approach 2:
#In this approach we will first sort the array and use two loops and use two pointers approach on remainder of the array and we wil use such logic tha
#we can avoid getting duplicate quadruplets

    def fourSum(self, nums, target):
        res = []
        i = 0
        n = len(nums)
        while i<n:
            j = i+1
            while j<n:
                low = j+1
                high = n-1
                while low<high:
                    if nums[i]+nums[j]+nums[low]+nums[high]==target:
                        temp = [nums[i], nums[j], nums[low], nums[high]]
                        res.append(temp)
                        
                        while low<high and nums[low]==nums[low+1]:
                            low+=1
                        while high>low and nums[high]==nums[high-1]:
                            high-=1
                        low+=1
                        high-=1
                    elif nums[i]+nums[j]+nums[low]+nums[high]>target:
                        high-=1
                    else:
                        low+=1
                while j<n-1 and nums[j]==nums[j+1]:
                    j+=1
                j+=1
            while i<n-1 and nums[i]==nums[i+1]:
                i+=1
            i+=1
        return res
    
    #Time Complexity: O(n**3)+O(nlogn)
    #Space Complexity: O(1)
    
    
    
