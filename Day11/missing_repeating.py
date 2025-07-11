#User function Template for python3

class Solution:
    def findTwoElement( self,arr): 
        mpp = {};
        repeating=0;
        missing = 0;
        n = len(arr);
        arr.sort();
        for num in arr:
            if num in mpp:
                mpp[num]+=1;
            else:
                mpp[num]=1;
        
        for i in range(1,n+1):
            if i not in mpp:
                missing = i;
            elif mpp[i] == 2:
                repeating = i;
                
        return [repeating,missing];
            
