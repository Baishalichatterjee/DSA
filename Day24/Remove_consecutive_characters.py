#User function Template for python3

class Solution:
    def removeConsecutiveCharacter(self, s):
        ans="";
        ans += s[0];
        n=len(s);
        for i in range(1,n):
            if s[i] != s[i-1]:
                ans+=s[i];
            else:
                continue;
        return ans;