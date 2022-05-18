#In this question we are given a matrix of m*n and it has sorted rows and last element of a row is lesser than first element of next row
#We have to find if given target is present in the matrix or not.

#Naive Approach:
#In ths approach we will traverse over whole matrix and try to find the target

class Solution(object):
    def searchMatrix(self, matrix, target):
        n = len(matrix)
        m = len(matrix[0])
        
        for i in range(n):
            for j in range(m):
                if matrix[i][j]==target:
                    return True
        return False
    
    #Time Complexity : O(n*m)
    #Space Complexity : O(1)
    
    

#Binary Search:
#As we know that array is sorted we will apply the procedure of binary sort to the array
    def searchMatrix(self, matrix, target):
        
        n = len(matrix)
        m = len(matrix[0])
        
        low = 0
        high = (m*n)-1
        
        if m==0:
            return False
        
        while low<=high:
            mid = low+((high-low)//2)               #high-low to find the span of whole to be traversed array, low is added to get to starting index fot this array
            
            if matrix[mid//m][mid%m]==target:       #mid//m and mid%m is simmilar to 22//10 = 2 tens and 22%10==2 ones
                return True
            if matrix[mid//m][mid%m]<target:
                low=mid+1
            else:
                high = mid-1
                
                
        return False
    
    #Time Complexity : O(log(m*n))
    #Space Complexity : O(1)
    
    
    #Another Approach:
    #In this approach we will traverse the columns from end and rows from beginning and if greater element is found we will reduce the column else increase row.
    
    class Solution:
	def matSearch(self,mat, N, M, X):
		i = 0
		j = M-1
		
		while i<n and j>=0:
		    if mat[i][j]==X:
		        return 1
		    elif mat[i][j]>X:
		        j-=1
		    else:
		        i+=1
		return 0
    
    #Time Complexity : O(max(n,m))
    #Space Complexity : O(1)
