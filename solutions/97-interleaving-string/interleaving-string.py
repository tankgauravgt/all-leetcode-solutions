class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        
        @cache
        def rec(p1, p2, p3):
            if p3 == len(s3):
                return p1 == len(s1) and p2 == len(s2)
            flag = False
            if p1 < len(s1) and s1[p1] == s3[p3]:
                flag = flag or rec(p1 + 1, p2, p3 + 1)
            if p2 < len(s2) and s2[p2] == s3[p3]:
                flag = flag or rec(p1, p2 + 1, p3 + 1)
            return flag

        return rec(0, 0, 0)