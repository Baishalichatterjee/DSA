class Solution:

    def majorityElement(self, nums: List[int]) -> int:

        n = len(nums);

        mpp = {};

        for num in nums:

            if num in mpp:

                mpp[num] += 1;

            else:

                mpp[num]=1;

                

        for key,value in mpp.items():

            if value > n/2:

                return key;