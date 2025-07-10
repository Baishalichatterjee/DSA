class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        mpp={0:1};
        prefix_sum=0;
        count=0;
        for num in nums:
            prefix_sum += num;
            if prefix_sum - k in mpp:
                count += mpp[prefix_sum - k];
            mpp[prefix_sum] = mpp.get(prefix_sum,0)+1;
        return count;
        