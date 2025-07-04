#brute force 
#TC->O(N+M);
#SC->O(N+M);
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        i=0;
        j=0;
        ans = [];
        while i<m and j<n:
            if nums1[i] < nums2[j]:
                ans.append(nums1[i]);
                i+=1;
            else :
                ans.append(nums2[j]);
                j+=1;
        
        while i<m:
            ans.append(nums1[i]);
            i+=1;
        
        while j<n:
            ans.append(nums2[j]);
            j+=1;
        
        k=0;
        for i in range(0,len(ans)):
            nums1[k]=ans[i];
            k+=1;
        

#another solution
#TC->O(N+M);
#SC->O(1);
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        i=m-1;
        j=n-1;
        k=m+n-1;
        while j>=0:
            if i>=0 and nums1[i] > nums2[j]:
                nums1[k] = nums1[i];
                i-=1;
            else :
                nums1[k]=nums2[j];
                j-=1;
            k-=1;