#In this question, given a string, we have to find the length of longest substring without repeating characters

#Naive approach:
#In this approach we use a set and two nested loops to generate every substring and check for repeating characters

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        maxlen = 0
        n = len(s)
        for i in range(n):
            hashSet = set()
            for j in range(i, n):
                if s[j] in hashSet:
                    maxlen = max(maxlen, j-i)
                    break
                set.insert(s[j])
                
        return maxlen
    
    
    #Time Complexity: O(n*n)
    #Space complexity: O(n)
    
    
#Optimized approach:
#In this approach, we will use two pointers, one will move ahead and store the encountered elements in the set and as a reoccuring element is encounterded another 
#pointer will move forward and delete the characters encountered by it, it will move forward until repeating character is deleted

    def lengthOfLongestSubstring(self, s):
        maxlen = 0
        n = len(s)
        hashSet = set()
        l = 0
        r = 0
        while r<n:
            if s[r] in hashSet:
                hashSet.remove(s[l])
                l+=1
            else:
                maxlen = max(maxlen, r-l+1)
                r+=1
        return maxlen
    
    #Time Complexity: O(2n)
    #Space Complexity: O(n)
    
    
#Optimized approach 2:
#In this approach instead of moving l one at a time, we will directly move it to index next to repeating element, to do this we use a dictionary to store index of 
#encountered elements as we go

     def lengthOfLongestSubstring(self, s):
        maxlen = 0
        n = len(s)
        hash = {}
        l = 0
        r = 0
        while r<n:
            if s[r] in hash and hash[s[r]]>=l:
                l = hash[s[r]]+1
            else:
                maxlen = max(maxlen, r-l+1)
            hash[s[r]] = r
            r+=1
        return maxlen
    
    
    #Time Complexity: O(n)
    #Space Complexity: O(n)
                
