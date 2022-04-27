#In this problem interviewer asks you to print the pascals triangle upto n rows in form of a 2d array.
#Furthermore, interviewer can ask also ask you to print out a single row and even a single element.

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
    #This is very natural method of printing Pascal's triangle.
    #Pascal's triangle is actually surrounded by infinite number of zeroes
    
        res = [[1]]
        #First integer in Pascal's triangle is one
    
        for i in range(numRows):
            temp = [0] + res[-1] + [0]
            sum = []
            for j in range(len(res[-1])+1):
                sum.append(temp[j] + temp[j+1])
            res.append(sum)
        return res
    
    #Time complexity for this approach is O(n*n).
    #Space complexity for this approach is also O(n*n). We created a 2D array of n rows and n columns.
    
#An another problem related to Pascal's Triangle is to find a induvidual number given its row and column in Pascal's triangle.
#We can do it by using combination method. 
#For any given row and column number we can get the desired number by (r-1)C(c-1).
    
def pascalNumber(r,c):
    number = 1
    while c>1:
        number = number*(r-1)/(c-1)
        c-=1
        r-=1
    return int(number)
    
    #Time Complexity of this approach is O(n).
    #Space Complexity of this approach is O(1)
    
    

#There is yet another type of question on Pascal's Triangle that could be asked in the interviews.
#In this problem we have to find out the entire row of Pascal's Triangle.
#This problem can be solved by finding induvidual numbers, but it cost us O(n*n) time complexity.
#Howevwer when we look at the question we find that 

def pascalRow(n):
    row = [1]
    number = 1
    for i in range(1,n):
        number = number*(n-i)/(i)
        row.append(int(number))
    return row
    
#Time Complexity of this approach is O(n).
#Space Complexity of this approach is also O(n)
        
        
