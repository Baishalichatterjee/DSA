

class Solution:
    def isRotated(self,s1,s2):
        left_rotation = s1[2:] + s1[:2];
        right_rotation = s1[-2:] + s1[:-2];
        if s2 == left_rotation or s2 == right_rotation :
            return True;
        return False;
            