class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        n=len(nums);
        start=0;
        end=n-1;
        if nums[end] < target:
            return end+1;
        while start <= end:
            mid = (start+end)//2;
            if nums[mid] == target:
                return mid;
            elif nums[mid] > target:
                end = mid-1;
            else:
                start = mid+1;
        return start;
        