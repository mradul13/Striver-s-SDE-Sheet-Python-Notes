#In this question we are given two sorted arrays and we have to merge them and sort them so that all smaller elements get stored in 1st array and larger in 2nd array

#Brute Force:
#First, we use a approach with using extra space
#In this approach, we use another array with size m+n and sort it with merge sort.

class Solution(object):
    def merge(self, nums1, m, nums2, n):
        new_arr = nums1 + nums2
        new_arr.sort()
        for i in range(m):
            nums1[i] = new_arr[i]
        for j in range(n):
            nums2[j] = new_arr[m+j]
            
    #Time Complexity : O(nlogn + n+n)
    #Space Complexity : O(n)
    
    
    #Without Using Space:
    #In this approach we will swap an element from 2nd array into 1st array if its found to be smaller, and then sort the 2nd array again so that we get sorted array 
    #in next Iteration.
    
    def merge(self, nums1, m, nums2, n):
        for i in range(m):
            
            if nums1[i]>nums2[0]:
                nums1[i], nums2[0] = nums2[0], nums1[i]
                j = 0
                while j<n-1:
                    if nums2[j]>nums2[j+1]:
                        nums2[j], nums2[j+1] = nums2[j+1], nums[j]
                        
    #Time Complexity : O(n*n)
    #Space Complexity : O(1)
    
    
    
    #The GAP method:
    #In this method we will take a gap of m+n/2 initially and check if first elements present in pointers which are apart from each other by gap,
    #is larger than the second one then we swap
    #If pointer runs out of index than we start agin by using gap = ceil(gap/2)
    
    #Solve this question on GFG
    class Solution:
    def merge(self, arr1, arr2, n, m):
        import math
        def gapf(n):
            if n==1:
                return 0
            return math.ceil(n/2)
       
        gap = m+n
        gap = gapf(gap)
        
        while gap>0:
            i = 0
            while i+gap<n:    #when both pointers is still in first array
                if arr1[i]>arr1[i+gap]:
                    arr1[i], arr1[i+gap] = arr1[i+gap], arr1[i]
                i+=1
            if gap>n:   
                j = gap-n    #if 2nd pointer directly goes to second array
            else:
                j = 0        #pointer goes to second array when 1st array is over
            
            while i<n and j<m:  #1st pointer in 1st arr and 2nd pointer in 2nd
                if arr1[i]>arr2[j]:
                    arr1[i], arr2[j] = arr2[j], arr1[i]
                i+=1
                j+=1
            
            if j<m:    #if 1st array exhausts first.
                j =0
                while j+gap<m:  #both pointers in 2nd array
                    if arr2[j]>arr2[j+gap]:
                        arr2[j], arr2[j+gap]= arr2[j+gap], arr2[j]
                    j+=1
            gap = gapf(gap)        #as 2nd arr also exaust gap is halved        
    
    
    #Time Complexity : O(log2n*n)
    #Space Complexity : O(1)
                        
                    
                    
                
