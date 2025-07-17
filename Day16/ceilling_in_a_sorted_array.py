#User function Template for python3
class Solution:
    def findCeil(self, arr, x):
        n=len(arr);
        start=0;
        end=n-1;
        ans = -1;
        while start <= end:
            mid = (start+end)//2;
            if arr[mid] < x:
                start = mid+1;
            else:
                ans = mid;
                end = mid - 1;
        return ans;
        
