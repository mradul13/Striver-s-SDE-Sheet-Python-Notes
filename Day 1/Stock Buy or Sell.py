#In this question, an array is given for the prices of stock and at ith day.
#We have to find the maximum profit we can get by only buying and selling the stock ones 



#Brute Force Approach:
#In this approach we generate all the possible buy and sell decisions by using two nested loops

class Solution(object):
    def maxProfit(self, prices):
        n = len(prices)
        max_pro = 0
        for i in range(n):
            for j in range(i,n):
                if prices[j]>prices[i]:
                    #Even if this if statement is not used, function will still return the coreect answer
                    max_pro = max((prices[j]-prices[i]), max_pro)
                
        return max_pro
        
    #Time Complexity : O(N*N)
    #Space Complexity : O(1)
    
    
    
    #Optimized Approach:
    #In this approach we will set a minimum first and then loop through the array and to check for a new minimum update it
    #If new element is not new minimum then set it as curr sum and chech if its greater than max, if yes than replace it.
    
    def maxProfit(self, prices):
        n = len(prices)
        max_pro = 0
        mini = prices[0]   #Minimum is set
        for i in range(n):
            if prices[i]<mini:
                mini = prices[i]
            else:
                max_pro = max((prices[i]-mini), max_pro)
        return max_pro
        
    
    #Time Complexity : O(N)
    #Space Complexity : O(1)
