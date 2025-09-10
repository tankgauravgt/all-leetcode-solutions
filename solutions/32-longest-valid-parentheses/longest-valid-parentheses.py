class Solution:
    def longestValidParentheses(self, s: str) -> int:
        
        N = len(s)
        
        if N < 2:
            return 0

        @cache
        def solve(sx):
            if sx <= 0:
                return 0

            clen = 0
            if s[sx] == '(':
                return clen
                        
            if s[sx - 1] == '(':
                clen = solve(sx - 2) + 2
            
            elif s[sx - 1] == ')':
                plen = solve(sx - 1)
                ox = sx - plen - 1
                if ox >= 0 and s[ox] == '(':
                    clen = plen + 2 + solve(ox - 1)
            
            return clen

        cmax = 0
        for ix in range(N):
            cmax = max(cmax, solve(ix))
        
        return cmax