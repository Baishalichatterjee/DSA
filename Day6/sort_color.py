class Solution:
    def sortColors(self, nums: List[int]) -> None:
        nums.sort();
        





#another solution
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        cnt0=0;
        cnt1=0;
        cnt2=0;
        n=len(nums);
        for i in range(0,n):
            if nums[i] == 0:
                cnt0+=1;
            elif nums[i]==1:
                cnt1+=1;
            else :
                cnt2+=1;

        k=0;
        while cnt0 > 0:
            nums[k] = 0;
            k+=1;
            cnt0 -= 1;
        while cnt1 > 0:
            nums[k]=1;
            k+=1;
            cnt1-=1;
        while cnt2 > 0:
            nums[k]=2;
            k+=1;
            cnt2-=1;
        

        