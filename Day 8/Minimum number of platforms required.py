#In this question, we are asked that given a railway station and arrays containing data about arrival and departure of the trains, calculate minimum
#number of platforms required

#Naive approach:
#In this approach we basically test that for every train that an if an train comes before the train we are checking for and leaves after the arrival of first train
#or if a train comes after the train we are checking for but departs after the arrival of the first train


class Solution:    
    #Function to find the minimum number of platforms required at the
    #railway station such that no train waits.
    def minimumPlatform(self,n,arr,dep):
        ans = 1
        for i in range(n):
            for j in range(i+1, n):
                if ar
