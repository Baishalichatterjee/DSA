class Solution:
    def isPossible(self, k, arr1, arr2):
        arr1.sort();
        arr2.sort(reverse=True);
        i=0;
        j=0;
        n=len(arr1);
        m=len(arr2);
        while i<n and j<m:
            if arr1[i]+arr2[j] < k :
                return False;
            i+=1;
            j+=1;
            
        return True;