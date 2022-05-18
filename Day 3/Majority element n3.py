#This question is extension of previous question in this question we have to return the elements which occur more than n//3 times

#Use brute force and Hashmap approach as previous question

#Extended Boyer Moore Voting algorithm:
#In this approach, we know that at max 2 elements can occur more than n/3 times, in general max k-1 distinct elements can occur more than n//k in an array

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        majmark = n//3
        count1 = 0
        count2 = 0
        ele1 = -1.5       #Always use such value for initialization which is not present in the given array
        ele2 = -1.5
        ans = []
        
        for i in range(n):
            if ele1==nums[i]:
                count1+=1
            elif ele2==nums[i]:
                count2+=1
            elif count1==0:
                ele1=nums[i]
                count1=1
            elif count2==0:
                ele2=nums[i]
                count2=1
            else:
                count1-=1
                count2-=1
        
        count1 = count2 = 0
        
        for i in range(n):
            if nums[i]==ele1:
                count1+=1
            if nums[i]==ele2:
                count2+=1
                
        if count1>majmark:
            ans.append(ele1)
        if count2>majmark:
            ans.append(ele2)
        
        return ans
    
    #Time Complexity: O(n)
    #Space Complexity: O(1)
