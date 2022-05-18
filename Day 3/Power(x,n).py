#In this question we have been asked to calculate x raised to power n, without using inbuilt functions

#NAive Approach:
#In this approach we will iterate n times and multiply x with ans(a variable)

class Solution(object):
    def myPow(self, x, n):
        if n<0:
            negflag = True
            n =n*(-1)
        ans = 1.0
        for i in range(n):
            ans = ans*x
            
        if negflag:
            return 1.0/ans
        else:
            return ans
      
    #Time Comlexity : O(n*n)
    #Space Complexity : O(1)
    
    
#Binary Exponentiation:
#In this approach we will use binary exponetiation whenever we find n divisible by 2, we set x = x*x and divide n by 2

class Solution(object):
    def myPow(self, x, n):
        nn = n
        if nn<1:
            nn*(-1)
        while nn:
            if nn%2:
                ans = ans*x
                nn-=1
            else:
                x= x*x
                nn= nn/2
            
        if n<0:
            return 1.0/ans
        else:
            return ans
        
   #Time Complexity : O(logn)
   #Space Complexity : O(1)
            
