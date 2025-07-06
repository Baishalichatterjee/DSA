class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums);
        maxInd = 0;
        for i in range(0,n):
            if maxInd < i:
                return False;
            maxInd = max(maxInd,nums[i]+i);
        return True;
        