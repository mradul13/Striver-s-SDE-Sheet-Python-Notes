# In this question we have to find the pairs which satisfy the following the conditions i<j and A[i]>2*A[j]

#Brute force approach:
#In this approach we will generate all possible pairs and count those which stisfy the conditions.

class Solution(object):    
    def reversePairs(self, nums):
        count = 0
        n = len(nums)
        for i in range(n-1):
            for j in range(i+1, n):
                if nums[i]>2*nums[j]:
                    count+=1
        
        return count
    
    
    #Time Complexity : O(n*n)
    #Space Complexity : O(1)
    

#Finding pairs with merge sort:
#In this approach similar to inversion counting we will use merge sort to find the reverse pairs

    def reversePairs(self, nums):
        def Merge(nums, temp, left, mid, right):
            revcount = 0
            j = mid+1
            for i in range(left, mid+1):
                while j<=right and nums[i]>2*nums[j]:
                    j+=1
                revcount+= j -mid-1
            
            j = mid+1
            i = left
            k = left
            
            while i<=mid and j<=rigth:
                if nums[i]<nums[j]:
                    temp[k]=nums[i]
                    k+=1
                    i+=1
                else:
                    temp[k]=nums[j]
                    k+=1
                    j+=1
                   
            while i<=mid:
                temp[k]=nums[i]
                k+=1
                i+=1
                
            while j<=right:
                temp[k]=nums[j]
                k+=1
                j+=1
                
            for i in range(len(nums)):
                nums[i]=temp[i]
                
            return revcount
        
        def MergeSort(nums, temp, left, right):
            revcount = 0
            if left<right:
                mid = (left+right)//2
                revcount+=MergeSort(nums, temp, left, mid)
                revcount+=MergeSort(nums, temp, mid+1, right)
                revcount+=Merge(nums, temp, left, mid, right)
                
            return revcount
        
        n = len(nums)
        temp = [0]*n
        return MergeSort(nums, temp, 0, n-1)
    
    #Time Complexity: O(NlogN) + O(N) + O(N)
    #Space Complexity: O(N)
