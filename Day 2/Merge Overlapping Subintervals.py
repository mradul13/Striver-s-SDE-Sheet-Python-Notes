#In this question we are given a array of intervals, we have to merge overlapping intervals.
#First ask the interviewer if the given array is sorted, if yes continue without sorting if not first sort it.

#Brut Force Approach:
#In this approach we iterate over each element by using to loops, and store the merged intervals in seperate array.

class Solution(object):
    def merge(self, intervals):
        intervals.sort()
        ans = []
        for i in range(len(intervals)):
            start = intervals[i][0]
            end = intervals[i][0]
            if !(ans.isempty()):
                if intervals[i][0]<ans[-1][1]:
                    continue
            for j in range(i+1, len(intervals)):
                if end>=intervals[j][0]:
                    end = intervals[j][1]
            ans.append([start, end])
       return ans
    
    #Time Complexity : O(nlogn + n*n)
    #Space Complexity : O(n)
    
    

    #Better Approach:
    #In this approach we will take a array variable to store the intervals, and then we traverse through interval array we check if there is overlap
    #If not we append the variable into answer array
    
    def merge(self, intervals):
        n = len(intervals)
        intervals.sort()
        ans = []
        out = intervals[0]
        for i in range(n):
            temp = intervals[i]
            if temp[0]<=out[1]:
                out[1] = max(temp[1], out[1])
            else:
                ans.append(out)
                out = temp
        ans.append(out)
        return ans
    
    #Time Complexity : O(nlogn + n)
    #Space Complexity : O(n)
