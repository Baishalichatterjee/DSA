
class Solution:
    def findIndex (self,arr, key ):
        n=len(arr);
        first=-1;
        second=-1;
        for i in range(0,n):
            if arr[i] == key:
                first=i;
                break;
        
        
        for i in range(n-1,-1,-1):
            if arr[i] == key:
                second = i;
                break;
        
        
        return [first,second];
        