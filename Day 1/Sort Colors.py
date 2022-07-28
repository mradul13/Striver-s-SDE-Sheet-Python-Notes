#In this question we are given an array of only zeroes, ones and twos, we have to sort the array.

#First Approach:
#In this approach we use common merge sort to sort the array

class Solution(object):
    def sortColors(self, nums):
        nums.sort()
      
    #Time Complexity : O(nlogn)
    #Space Complexity : O(n)
    
    
    #Second Approach :
    #In this approach we can create a frequency array or hashmap, since the number of different elements present in array are known i.e 0, 1 and 2
    #Then we can use the frequency array to rewrite the array in sorted manner.
    
    def sortColors(self, nums):
        freq_arr0 = 0
        freq_arr1 = 0
        freq_arr2 = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                freq_arr0 += 1
            if nums[i] == 1:
                freq_arr1 += 1
            if nums[i] == 2:
                freq_arr2 += 1
        
        for i in range(len(nums)):
            if freq_arr0!=0:
                nums[i] = 0
                freq_arr0-=1
            else:
                if freq_arr1!=0:
                    nums[i]=1
                    freq_arr1-=1
                else:
                    nums[i] = 2
       
    
    #Time Complexity : O(N+N)
    #Space Complexity : O(1)
    
    
    #Dutch Flag algorithm
    #In this approach we use three pointers low, mid and high and mid moves and checks is index values
    #If index value is 1, then mid just moves forward
    #If index value is 0, then it swaps with low, and both low and mid moves forward
    #If index value is 2, then it swaps with high and high moves backwards
    #In this manner all zeroes get collected in left side all, twos get collected to right side.
    
    def sortColors(self, nums):
        low = 0
        mid = 0
        high = len(nums) - 1
        
        while mid<high:
            if nums[mid]==0:
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1
            elif nums[mid] == 1:
                mid+=1 
            elif nums[mid] == 2:
                nums[mid], nums[high] = nums[high], nums[mid]
                high -= 1
                
   #Time Complexity : O(N)
   #Space Complexity : O(1)
      
