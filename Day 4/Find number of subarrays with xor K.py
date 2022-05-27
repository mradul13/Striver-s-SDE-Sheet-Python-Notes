#In this question we are given an integer and an array and we have to find the number of subarrays with xor eqaul to given integer

#Brute Force approach:
#In this approach we will generate all possible subarrays and check if thier xor equals to target

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        count = 0
        for i in range(len(A)):
            xor = 0
            for j in range(i, len(A)):
                xor = xor^A[i]
            if xor == B:
                count+=1
        return count
    
    #Time Complexity: O(n*n)
    #Space Complexity: O(1)
    
    
#Prefix xor and map approach:

#In this approach we observe the already xor prefix in a hashmap and if any where we find a prefix = running xor^B, then it means that subarray from prefix index to 
#running index is an sub array with xor = target
#Let Q = Xor of elements upto q
#Let P = Xor of elements upto p and including numbers upto q
#if P^target = Q
#P^target^P = Q^P
#target = Q^P

    def solve(self, A, B):
        count = 0
        xor = 0
        hash ={}
        for i in range(len(A)):
            xor = xor^A[i]
            if xor^B in hash:
                count +=hash[A[i]]
            if xor ==target:
                count+=1
            if xor in hash:
                hash[A[i]]+=1
            else:
                hash[A[i]]=1
        return count
    
    #Time Complexity: O(n)
    #Space Complexity: O(n)
