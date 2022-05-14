#In this question, we are given an array of n size which contains one repeating number and one missing number, we have to find these two numbers.

#Brute Force approach:
#In this approach we take an frequency array and then traverse the frequency array and find the missing and repeating number.

class Solution:
    def findTwoElement( self,arr, n):
        freq = [0]*(n+1)
        ans = [0, 0]
        for i in range(n):
            freq[arr[i]]+=1
            
        for i in range(1,n+1):
            if freq[i] ==2:
                ans[0]= i
            elif freq[i] ==0 :
                ans[1] = i
        
        return ans
    
    #Time Complexity : O(n) + O(n)
    #Space Compexity : O(n)
      
    
    
    #Using Maths:
    #The idea is to convert the problem into equations:
    #Equation for sum of n numbers, S = n(n+1)/2
    #Equation for sum of squares of n numbers, P = n(n+1)(2n+1)/6
    #Let s1 be sum of array and p1 be sum of squares of array.
    #X-Y = s-s1 = s`
    #(X+Y)(X-Y) =p-p1= p`
    #X+Y - p`/s`
    
    def findTwoElement( self,arr, n):
        S = (n*(n+1))/2
        P = (n*(n+1)*((2*n)+1))/6
        
        for i in range(n):
            S-= arr[i]
            P-= (arr[i]*arr[i])
            
        ans = []
        miss = (S+P/S)/2
        rep = miss - S
        
        ans.append(rep)
        ans.append(miss)
        
        return ans
    
    #Time Compexity : O(n)
    #Space Complexity : O(1)
    
    
    #XOR Approach:
    #In this approach, we use properties of XOR operator to find out the missing and repeating numbers.    
    #We XOR of all numbers in array and XOR of all numbers upto n, and then then divide two sets of XOR to find the numbers
    
    def findTwoElement( self,arr, n):  
      
        XOR = 0
        x = 0
        y = 0
        ans= []
        for i in range(n):
            XOR = XOR^arr[i]
            
        for i in range(1,n+1):
            XOR = XOR^i
        
        last_set_bit = XOR & ~(XOR-1)
        
        for i in range(n):
            if (arr[i]&last_set_bit):
                x = x^arr[i]
            else:
                y = y^arr[i]
                
        for i in range(1, n+1):
            if (i&last_set_bit):
                x = x^i
            else:
                y = y^i
        
        count = 0
        for i in range(n):
            if arr[i]==x:
                count+=1
            
        if count ==2:
            ans.append(x)
            ans.append(y)
        else:
            ans.append(y)
            ans.append(x)
            
        return ans
    
    #Time Compleity : O(n)
    #Space Complexity : O(1)
