class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        st = set()
        for num in nums:
            st.add(num);
        index=0;
        for val in sorted(st):
            nums[index] = val;
            index += 1;
        return index;





class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n=len(nums);
        i=0;
        for j in range(1,n):
            if nums[j] != nums[i]:
                nums[i+1] = nums[j];
                i+=1;
        return i+1;
        