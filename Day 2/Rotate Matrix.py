#In this question we are given a square matrix and we have to rotate it by 90 degrees clokwise.

#Brute Force Approach:
#In this approach we take another matrix and put the first row of given matrix in last column of this new matrix and so on.

class Solution(object):
    def rotate(self, matrix):
        n = len(matrix)
        new_mat = [[0]*n]*n
        for i in range(n):
            for j in range(n):
                new_mat[j][n-1-i] = matrix[i][j]
        return new_mat
    
    #In leetcode question explicitly tells not to take another matrix.
    
    #Time Complexity = O(n*n)
    #Space Complexity = O(n)
    
    
    #Better Approach:
    #In this approach, we will take transpose of matrix(transpose of matrix is when rows and columns are interchanged)
    #Then after reversing to rows of transpose we get the desired output.
    
    def rotate(self, matrix):
        n = len(matrix)
        for i in range(n):
            for j in range(i,n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        #Now reverse the rows
        for i in range(n):
            for j in range(n//2):
                matrix[i][j], matrix[i][n-j-1] = matrix[i][n-j-1], matrix[i][j]
                
        #Time Complexity : O(n*n + n*n)
        #Space Complexity : O(1)
                
