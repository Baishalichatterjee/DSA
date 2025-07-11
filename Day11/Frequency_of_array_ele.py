class Solution:
    def frequencyCount(self, arr):
        mpp = {};
        n = len(arr);
        ans = [];
        for num in arr:
            if num in mpp:
                mpp[num] +=1;
            else:
                mpp[num]=1;
        
        for i in range(1,n+1):
            if i not in mpp:
                ans.append(0);
            else:
                ans.append(mpp[i]);
        
        return ans;
                
