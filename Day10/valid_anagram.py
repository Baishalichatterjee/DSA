class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        mpp={};
        for c in s:
            mpp[c]=mpp.get(c,0)+1;
        for c in t:
            mpp[c] = mpp.get(c,0)-1;
        for key,values in mpp.items():
            if values != 0:
                return False;
        return True;

        