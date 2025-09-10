class Solution:
    def climbStairs(self, n):

        @cache
        def rec(k):
            if k >= n:
                return k == n
            takeit = rec(k + 1)
            skipit = rec(k + 2)
            return takeit + skipit

        return rec(0)