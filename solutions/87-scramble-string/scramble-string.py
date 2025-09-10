from functools import lru_cache

class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        
        @lru_cache(None)
        def split(src, tgt):
            if src == tgt:
                return True
            if len(src) != len(tgt):
                return False
            
            n = len(src)
            for ix in range(1, n):  # Split at every possible position
                # Check without swapping
                if split(src[:ix], tgt[:ix]) and split(src[ix:], tgt[ix:]):
                    return True
                # Check with swapping
                if split(src[:ix], tgt[n - ix:]) and split(src[ix:], tgt[:n - ix]):
                    return True
            
            return False
        
        return split(s1, s2)