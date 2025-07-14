class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        haylen = len(haystack);
        needlen = len(needle);
        i=0;
        needindx=0;
        while i < haylen:
            if haystack[i] == needle[needindx]:
                needindx+=1;
                i+=1;
                if needindx == needlen:
                    return i-needlen;
            else:
                i = i-needindx+1;
                needindx=0;

        return -1;

        