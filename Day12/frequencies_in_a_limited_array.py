class Solution:
    def frequencyCount(self, arr):
        arr.sort();
        mpp = {};
        ans = [];
        for num in arr:
            if num in mpp:
                mpp[num] += 1;
            else:
                mpp[num]=1;
        
        n = len(arr);
        for i in range(1,n+1):
            if i in mpp:
                ans.append(mpp[i]);
            else:
                ans.append(0);
        
        return ans;
                

