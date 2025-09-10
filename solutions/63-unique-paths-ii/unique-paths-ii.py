class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        nR, nC = len(obstacleGrid), len(obstacleGrid[0])

        if obstacleGrid[0][0] == 1:
            return 0

        @cache
        def rec(m, n):
            if obstacleGrid[m][n] == 1:
                return 0
            if m == 0 and n == 0:
                return 1
            if m == 0:
                return rec(m, n - 1)
            if n == 0:
                return rec(m - 1, 0)
            return rec(m - 1, n) + rec(m, n - 1)
        
        return rec(nR - 1, nC - 1)