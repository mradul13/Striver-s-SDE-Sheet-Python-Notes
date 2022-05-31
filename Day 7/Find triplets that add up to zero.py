#In this question we are given an array, we have to find unique triplets that add up to 0

#Brute Force approach:
#In this approach we generate all possible triplets and store the ones adding to zero in a set to find unique triplets

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = set()
        n = len(nums)
        for i in range(n):
            for j in range(i+1, n):
                for k in range(j+1, n):
                    if nums[i]+nums[j]+nums[k]==0:
                        temp = [nums[i], nums[j], nums[k]]
                        res.add(temp)
        return list(res)
    
    #Time Complexity: O(n**3)
    #Space Complexity: O(3*k) k is number of triplet
    
    
#Hashing:
#You can optimize above approach by first hashing all the elements and then running two loops and checking if the compliment to thier addition is in hashtable

#Optimized approach:
#In this approach we first sort the array and then make one variable constant through a loop and then use two pointers method in rest of the array, also we use
#such logic that the duplicates are skipped over, this way we save the space of a hashset

def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        n = len(nums)
        nums.sort()
        i = 0
        res = []
        while i<n-2:
            if i==0 or (i>0 and nums[i]!=nums[i-1]):
                sum = 0-nums[i]
                low = i+1
                high = n-1
                while low < high:
                    if nums[low]+nums[high]==sum:
                        temp = [nums[i], nums[low], nums[high]]
                        res.append(temp)
                
                        while low<high and nums[low]==nums[low+1]:
                            low+=1
                        while low<high and nums[high]==nums[high-1]:
                            high-=1
                        low+=1
                        high-=1
                    elif nums[low]+nums[high]<sum:
                        low+=1
                    else:
                        high-=1
            i+=1
        return res
    
    #Time Complexity: O(n*n)    
    #space Complexity: O(m)   
    
