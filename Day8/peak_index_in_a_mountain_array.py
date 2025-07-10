class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        ans = 0;
        n = len(arr);
        start = 0;
        end = n-1;
        while start <= end:
            mid = (start + end)//2;
            if (arr[mid] > arr[mid+1] and arr[mid] > arr[mid-1]):
                return mid;
            elif arr[mid+1] > arr[mid] :
                start = mid+1;
            else:
                ans = mid;
                end = mid-1;
        return ans;

        