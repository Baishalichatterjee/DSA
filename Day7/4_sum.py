class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums);
        nums.sort();
        ans=[];
        st = set();
        for i in range(0,n-2):
            for j in range(i+1,n-1):
                new_target = target - nums[i] - nums[j];
                k=j+1;
                l=n-1;
                while k < l:
                    sum = nums[k] + nums[l];
                    if sum == new_target:
                        quard = (nums[i],nums[j],nums[k],nums[l]);
                        if quard not in st:
                            st.add(quard);
                        k+=1;
                        l-=1;
                    elif sum > new_target:
                        l-=1;
                    else:
                        k+=1;
        for it in st:
            ans.append(list(it));
        return ans;


        