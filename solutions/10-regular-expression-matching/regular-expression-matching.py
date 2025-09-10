class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        
        @cache
        def rec(s1, p1):
            # boundary conditions:
            if s1 > len(s) or p1 > len(p):
                return False
            if p1 == len(p):
                return s1 == len(s)
            
            # check if pattern is matching:
            matched = (s1 < len(s) and p1 < len(p)) and p[p1] in {'.', s[s1]}
            
            if p1 + 1 < len(p) and p[p1 + 1] == '*':
                take_it = rec(s1 + 1, p1)
                skip_it = rec(s1, p1 + 2)
                return (matched and take_it) or skip_it
            elif matched:
                return rec(s1 + 1, p1 + 1)
            
            return False
        
        return rec(0, 0)