#User function Template for python3

class Solution:
    def firstRepChar(self, s):
        n=len(s);
        mpp={};
        ans="";
        for ch in s:
            if ch in mpp:
                return ch;
            else:
                mpp[ch]=1;
        return "-1";