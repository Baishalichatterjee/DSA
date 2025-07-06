class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        ans  = [];
        mpp = {};
        n  = len(nums);
        for num in nums:
            if num in mpp:
                mpp[num]+=1;
            else:
                mpp[num]=1;
        for key,value in mpp.items():
            if value >= 2:
                ans.append(key);
        return ans;

        