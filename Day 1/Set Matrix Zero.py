class Solution:
#First we try brute force approach.
#We should always ask the Interviewer that if the input contains of negatives.
    def setZeroesBrute(self, matrix: List[List[int]]) -> None:
        rows = len(matrix)
        cols = len(matrix[0])
        
        for row in range(rows):
            for col in range(cols):
            #check if the element is zero or not
                if matrix[row][col] == 0:
                #if it is a zero loop through its rows and then columns and change all elements to -1 except 0.
            
                    for i in range(cols):
                    #column number must change but row number must remain constant to change the row
                        if matrix[row][i] != 0:
                            matrix[row][i] = -1
                        
                    for j in range(rows):
                    #row number must change but column number must remain constant to change a column
                        if matrix[j][col] != 0:
                            matrix[j][col] = -1
                    
        #Now we must again traverse the matrix to change all -1s to 0s
        for row in range(rows):
            for col in range(cols):
                if matrix[row][col] == -1:
                    matrix[row][col] = 0
        
        #Time Complexity for this approach is O((m*n)*(m+n)) + O(m*n). m*n for traversing in matrix and m+n for traversing in rows and cols.
        #Space Complexity for this approach is O(1). Matrix has been changed in place.
        
    def setZeroesExtraSpace(self, matrix: List[List[int]]) -> None:
    #In this approach we create two dummy arrays to keep track which rows and cols have zero in them.
    #This will decrease time compexity, but incfease space complexity.
        
        rows = len(matrix)
        cols = len(matrix[0])
        darrayrow = [-1]*(rows)
        darraycol = [-1]*(cols)
        
        for row in range(rows):
            for col in range(cols):
                if matrix[row][col] == 0:
                    darrayrow[row] = 0
                    darraycol[col] = 0
                    
        for row in range(rows):
            for col in range(cols):
                if darrayrow[row]==0 or darraycol[col]==0:
                #check if the element's row or column is in dummy array.
                    matrix[row][col] = 0
                    
        #Time Complexity for this approach is O(n*m) + O(n*m). Because we traversed matrix twice.
        #Space Complexity for this approach is O(n+m). We create dummy arrays of size n and m.
        
        
    def setZeroes(self, matrix: List[List[int]]) -> None:
    #This is the optimized approach. In this approach we take first row and column to store the metadata about zeroes.
    #We store metadata about rows in col1 and that about cols in row1.
    #We also take two variables to know whether first row or column itself contain zero and use them later.
    
        
        isrow0 = False
        iscol0 = False
        rows = len(matrix)
        cols = len(matrix[0])
        
        for row in range(rows):
            for col in range(cols):
                if matrix[row][col]==0:
          
                    if row ==0:
                        isrow0 = True
                    if col ==0:
                        iscol0 = True
                    elif row!=0 and col!=0:
                    #if row and column both are not first row, than we change chnage the first column if its a row and vice versa.
                        matrix[row][0]=0
                        matrix[0][col]=0
                    
        for row in range(1, rows):
            for col in range(1, cols):
            #Traverse the remainder of matrix and check if thier corresponding row or column is 0.
                if matrix[row][0]==0 or matrix[0][col]==0:
                    matrix[row][col]=0
        
        #check whether row or column themselves contained zero           
        if isrow0:
            matrix[0]= [0]*cols
        if iscol0:
            for row in range(rows):
                matrix[row][0]=0
                
        #Time Complexity for this approach is O(n*m) + O(n*m).
        #Space Complexity for this approach is O(1). We change matrix in place
                    
