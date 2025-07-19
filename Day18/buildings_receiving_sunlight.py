#User function Template for python3

class Solution:
    def longest(self, arr):
        n=len(arr);
        building=0;
        cnt=0;
        for i in range(0,n):
            if arr[i] >= building:
                building = arr[i];
                cnt+=1;
        
        
        return cnt;
    
