#In this question we have to return the next permutation in lexicographical order.

#Brute force 
#In this approach we can generate all permutation using recursion and store them in a list.
#Then we find given array and print the one next to it.
#We will look at this approac in recursion topic in SDE sheet.
#Time Complexity = O(n!*n)
#Space Complexity = O(1) + O(n!) (For stack)

#Better Approach
#Intuition behind this approach is not clear but we see a pattern that in permutations of a given set there's always a increasing subsequence that peaks somewhere
#We have to find that peak and replace item that is just greater than it and then reverse the array from peak index to end. 
#If there is no peak than its the last permutation, therefore return the reverse of the array.

class Solution(object):
    def nextPermutation(self, nums):
        n = len(nums)
        i = n-1
        #Search for such a index from backwards where its next index is greater in value(peak of the increasing subsequence). 
        while i>0:
            if nums[i]>nums[i-1]:
                break
            i-=1
        
        #If loop ends without peak then, just reverse the array
        if i ==0:
            nums = nums.reverse()
        else:
            j = n-1
            var1 = i-1
            #i-1 is used because i was the peak but we have to take one index lesser than the peak
            while nums[j]<=nums[var1]:
            #Find a number larger than the peak
                j-=1
            
            #Swap the peak an the number larger than the peak
            nums[var1], nums[j] = nums[j], nums[var1]
            
            #After swapping the numbers, reverse the array from peak index to the end
            var1 = i 
            j = n-1
            while j>var1:
                nums[var1], nums[j] = nums[j], nums[var1]
                j-=1
                var1+=1
                
        #You might have noticed that what we actually did is that we found the peak of given set, 
        #than we reduced its peak in index by replacing it wit value just larger than it, essentially creating a new peak of increasing subsequence.
            
        #Time Complexity = O(3*N) >> O(N)
        #Space Complexity = O(1)
        
      
