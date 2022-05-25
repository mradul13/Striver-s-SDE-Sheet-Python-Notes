#In this question interviewer asks us to find a pair in an array whose sum equals to given target.

#Brute Force Approach:
#In this approach we find all possible pairs and check for thier sum.
class Solution(object):
    def twoSum(self, nums, target):
        ans = []
        n = len(nums)
        for i in range(n):
            for j in range(i+1, n):
                if nums[i] + nums[j] == target:
                    ans.append(i)
                    ans.append(j)
                    break
            if len(ans)==2:
                break
                
        return ans
      
#Time Complexity : O(n*n)
#Space Complexity : O(1)


#Two pointer approach:
#In this method we first sort the array and then we use two pointers 
    def twoSum(self, nums, target):
        ans = []
        nums.sort()
        left = 0
        right = len(nums)-1
        while left<right:
            if nums[left]+nums[right]==target:
                ans.append(left)
                ans.append(right)
            elif nums[left]+nums[right]>target:
                right-=1
            else:
                left+=1
                
        return ans

#Time Complexity : O(nlogn)
#Space Complexity : O(n)


#Hashing:
#In this approach we will take a python dictionary and store the element encountered and in a loop check if its compliment is already in hashmap.

    def twoSum(self, nums, target):
        hash = {}
        ans = []
        for i in range(len(nums)):
            if target-nums[i] in hash:
                ans.append(i)
                ans.append(hash[target-nums[i]])
                break
            else:
                hash[nums[i]]=i
        return ans
      
#Time Complexity: O(n)
#Space Complexity : O(n)
            
    
    
