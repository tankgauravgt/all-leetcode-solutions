class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        
        # @cache
        # def sseq(sx, tx):
        #     if tx == len(t): return 1
        #     if sx == len(s): return 0
        #     count = 0
        #     if s[sx] == t[tx]:
        #         count = count + sseq(1 + sx, 1 + tx)
        #     count = count + sseq(1 + sx, tx)
        #     return count

        nS = 1 + len(s)
        nT = 1 + len(t)

        grid = [[0] * nS for _ in range(nT)]
        grid[0][0] = 1

        for tx in range(1, nT):
            grid[tx][0] = 0

        for sx in range(1, nS):
            grid[0][sx] = 1

        for tx in range(1, nT, 1):
            for sx in range(1, nS, 1):
                if s[sx - 1] == t[tx - 1]:
                    grid[tx][sx] += grid[tx - 1][sx - 1]
                grid[tx][sx] += grid[tx][sx - 1]
                        
        return grid[nT - 1][nS - 1]