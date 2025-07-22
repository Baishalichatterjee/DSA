class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        haylen = len(haystack);
        needlen = len(needle);
        needindx=0;
        i=0;
        while i<haylen:
            if haystack[i] == needle[needindx]:
                needindx+=1;
                i+=1;
                if needlen == needindx:
                    return i-needlen;
            else:
                i = i-needindx;
                needindx=0;
                i+=1;
        return -1;
        