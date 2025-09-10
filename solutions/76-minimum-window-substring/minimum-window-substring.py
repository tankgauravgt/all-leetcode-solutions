from collections import Counter
import math

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        if not t or not s: 
            return ""
        
        lx = 0
        rx = 0
        
        tgt = Counter(t)
        needed = len(tgt)

        src = {}        
        formed = len(src)

        out = None
        cmin = math.inf
        for rx, c in enumerate(s):

            # greedily append characters:
            src[c] = src.get(c, 0) + 1
            
            # increase formed counts:
            if c in tgt and src[c] == tgt[c]:
                formed = formed + 1

            # contract window until mismatch from left side:
            while lx <= rx and formed == needed:
                
                c = s[lx]

                if cmin > rx - lx + 1:
                    cmin = min(cmin, rx - lx + 1)
                    out = s[lx:rx + 1]
                
                src[c] = src[c] - 1

                if c in tgt and src[c] < tgt[c]:
                    formed = formed - 1

                lx = lx + 1
        
        return "" if not out else out