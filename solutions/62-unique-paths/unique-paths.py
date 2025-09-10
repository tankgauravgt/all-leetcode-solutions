import math

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        @cache
        def rec(m, n):
            if m == 1 or n == 1:
                return 1
            return rec(m - 1, n) + rec(m, n - 1)
        
        return rec(m, n)