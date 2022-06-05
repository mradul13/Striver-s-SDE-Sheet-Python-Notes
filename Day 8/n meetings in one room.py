#In this question we are asked that given a room in a company, in which meetings have to be held, we are given an array having starting and end timings
#of each meeting, we have to calculate maximum number meetings that can be held in that room

#Greedy approach:
#Our thought process is that the sooner the each meeting ends more meetings we can held, hence we sort the given array on basis of the end times
#then we iterate over and if we find that the end time of previous meeting is less than start time, we add one to max meetings counter.

class Solution:
    
    #Function to find the maximum number of meetings that can
    #be performed in a meeting room.
    def maximumMeetings(self,n,start,end):
        timings = list(zip(start, end)
        timings = sorted(timings, key = lambda x : x[1])
        a = times[0][1]
        count = 1
        for i in range(1,n):
            if times[i][0]>=a:
                count+=1
                a = times[i][1]
        return count
                       

    #Time Complexity: O(n)+O(nlogn)+O(n)>>O(n)
    #Space Complexity: O(n)
                       
                       
