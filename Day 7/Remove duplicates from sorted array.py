#In this question we are given a sorted array and we have to return the array with all distinct elements occupying the first indexes

#Brute Force Approach:
#In this approach we take a hashset and push all elements in it and then take length of set and push set elements into sorted array

class Solution(object):
    def removeDuplicates(self, nums):
        hashSet = set()
        for i in range(len(nums)):
            hashSet.add(nums[i])
        k = len(hashSet)
        hashSet = list(hashSet)
        for i in range(k):
            nums[i]=hashSet[i]
        return k
    
    #Time Complexity: O(n) +  O(n)
    #Space Complexity: O(n)
    
    
#Two pointer approach:
#In this approach we take two pointers and if we find values at those pointers unequal we will increase pointer1 and store the value of pointer2 in pointer1

    def removeDuplicates(self, nums):
        i = 0
        for j in range(1,len(nums)):
            if nums[i]!=nums[j]:
                i+=1
                nums[i]=nums[j]
        return i+1
    
    
    #Time Complexity: O(n)
    #Space Complexity O(1)
