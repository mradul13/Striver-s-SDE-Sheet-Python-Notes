#In this question we are given an array representing building height and rain water can we trapped between buildings.

#Brute force appraoch:
#In this approach we calculate leftmax and rightmax for every element and then take minimum of those and subtracting the height of current index add to reserve.

class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        res = 0
        n = len(height)
        for i in range(n):
            leftMax = 0
            rightMax = 0
            j =i
            while j>=0:
                leftMax = max(leftMax, height[j])
                j-=1
            j = i
            while j<n:
                rightMax = maxx(rightMax, height[j])
                j+=1
            res = min(righMax, leftMax)-height[i]
            
        return res
    
    #Time Complexity: O(n*n)
    #Space Complexity: O(1)
    
    
#Better approach:
#In this approach we before hand create prefix max and suffix max arrays and when traversing through the array check thier values to know trapped water

    def trap(self, height):
        n = len(height)
        prefix = [0]*n
        suffix = [0]*n
        prefix[0] = height[0]
        suffix[n-1] = height[n-1]
        for i in range(1, n):
            prefix[i] = max(prefix[i-1], height[i])
        for i in range(n-2, -1, -1):
            suffix[i] = max(suffix[i+1], height[i]
        for i in range(n):
            res+= min(prefix[i], suffix[i])-height[i]
        return res
        
                            
    #Time Complexity: O(n)+O(n)+O(n)
    #Space Complexity: O(2n)
                            
                            
#Optimal Approach:
#In this approach we will use two pointers, each maintaining either maxright or maxleft and the trapped water can be calculated by using them

    def trap(self, height):
		n = len(height)
        left = 0
        right = n-1         
        res = 0
        maxLeft = 0
        maxRight = 0        
        while left<=right:        
            if height[left]<=height[right]:                    
                if height[left]>=maxLeft:
                    maxLeft = height[left]
                else:
                    res+=maxLeft-height[left]
                left+=1
            else:
                if height[right]>=maxRight:
                    maxRight = height[right]
                else:
                    res+=maxRight-height[right]
                right-=1
        return res
        
    #Time Complexity: O(n)
    #Space Complexity: O(1)
                            
                            
                            
                          
