class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        n=len(nums);
        ans = [];
        cnt=0;
        for num in nums:
            if num == 0:
                cnt+=1;
            else:
                ans.append(num);
        while cnt != 0:
            ans.append(0);
            cnt-=1;
                
        k=0;
        m=len(ans);
        for i in range(0,m):
            nums[k]=ans[i];
            k+=1;
        