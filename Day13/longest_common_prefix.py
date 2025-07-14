class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans="";
        for i in range(len(strs[0])):
            ch = strs[0][i];
            matched = True;
            for j in range(1,len(strs)):
                if i>=len(strs[j]) or ch != strs[j][i]:
                    matched=False;
                    break;
            
            if matched == False:
                break;
            else:
                ans+=ch;


        return ans;


        