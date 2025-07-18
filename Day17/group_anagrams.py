class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mpp = {};
        ans = [];
        for word in strs:
            temp = ''.join(sorted(word));
            if temp not in mpp:
                mpp[temp] =[];
            mpp[temp].append(word);
        
        for key,values in mpp.items():
            ans.append(values);
        return ans;
        