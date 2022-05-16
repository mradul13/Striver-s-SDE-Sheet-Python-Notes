#In this question, we have to find inversions i.e. A[i]>A[j] when i<j;
#Number of inversions usually tell us how far is an array from being sorted.

#Approach:
#In this approach we will use a variation of mergeSort to count the inversions whenever we find arr[j]<arr[i].

class Solution:
    #User function Template for python3
    
    # arr[]: Input Array
    # N : Size of the Array arr[]
    #Function to count inversions in the array.
    def mergeSort(self,arr,n,invcount):
        if n==1:
            return 0
        mid = (len(arr))//2
        Left = arr[:mid]
        Right = arr[mid:]
        leftlen = len(Left)
        rightlen = len(Right)
        
        invcount += self.mergeSort(Left,leftlen, invcount)+self.mergeSort(Right,rightlen, invcount)
        
        i = j = k =0
        
        while i<leftlen and j<rightlen:
            if Left[i]<Right[j]:
                arr[k]=Left[i]
                i+=1
            else:
                arr[k]= Right[j]
                j+=1
                invcount+= (mid-i)
                #Count all the numbers right.
            k+=1
        
        #For remaining elements in either left or right
        while i<leftlen:
            arr[k]=Left[i]
            i+=1
            k+=1
        while j<rightlen:
            arr[k]=Right[j]
            j+=1
            k+=1
        return invcount

    def inversionCount(self, arr, n):
        invcount=0
        return self.mergeSort(arr,n,invcount)
    
    #Time Complexity: O(nlogn)
    #Space Complexity : O(n)
