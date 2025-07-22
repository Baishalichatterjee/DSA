class Solution:
    def check(self,s:str,i:int,j:int):
        while i<=j:
            if s[i]!=s[j]:
                return False;
            i+=1;
            j-=1;
        return True;
    def validPalindrome(self, s: str) -> bool:
        n=len(s);
        i=0;
        j=n-1;
        while i<=j:
            if s[i] != s[j]:
                return self.check(s,i+1,j) or self.check(s,i,j-1);
            i+=1;
            j-=1;
        return True;
        