#In this question we have to find out number of possible paths from top left to right botton, given that we can move only right and down.


#Recursive approach:
#In this approach we will take base cases as reaching the bottom right and going out of inde or we recursively call the function.

class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        
        def countPaths(i, j, m, n):
            if i==m-1 and j==n-1:                                           #End point reached, 1 path confirmed
                return 1
            if i>=m or j>=n:                                                #Out of index
                return 0
            else:
                return countPaths(i+1, j, m, n) + countPaths(i, j+1, m, n)
            
        return countPaths(0, 0, m, n)
    
    #Time Complexity : O(2**n) Exponential as each non base case calls two other cases
    #Space Complexity : O(2**n)
    
    
#Dynamic programming Approach:
#As seen in recursive approach, a lot of cases are repeated and to avoid this repetition, we store the answers of prviously visited cases in a table
#And use that data to instantly know the answer of repeated case
    
    def uniquePaths(self, m, n):
        dp = [[-1 for i in range(n)] for i in range(m)]
        def countPaths(i, j, m , n, dp):
            if i==m-1 and j==n-1:
                return 1
            if i>=m or j>=n:
                return 0
            if dp[i][j]!=-1:
                return dp[i][j]
            else:
                dp[i][j] =countPaths(i+1, j, m, n, dp)+countPaths(i, j+1, m, n, dp)
                return dp[i][j]
        
        
        return countPaths(0, 0, m, n, dp)
    
    #Time Complexity: O(n*m) Only m*n states possible
    #Space Complexity: o(n*m)
    
    
#Combinatorics:
#In this approach we will apply combinatorial to the problem
#we come to observe that in any given grid we can move m-1 times down and n-1 times right, also in a given grid we can only move m-1+n-1 = m+n-2.
#Now the only task is to arrange these moves in unique order.
#Consider 2*2 mat, we can only do 2 moves DR and RD.

    def uniquePaths(self, m, n):
        Tmoves = m+n-2
        Rmoves = m-1
        paths = 1
        for i in range(1, Rmoves+1):
            paths = paths*(Tmoves+i-Rmoves)/i
            
        return int(paths)
    
    #Time Complexity : O(n-1) or O(m-1)
    #Space Complexity : O(1)
