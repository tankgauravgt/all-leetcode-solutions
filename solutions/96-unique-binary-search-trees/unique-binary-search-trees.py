import math
class Solution:
    def numTrees(self, n: int) -> int:

        @cache
        def rec(k):
            if k < 2: return 1
            total = 0
            for ix in range(k):
                total = total + rec(k - ix - 1) * rec(ix)
            return total
        return rec(n)