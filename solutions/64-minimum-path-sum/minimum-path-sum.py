class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        nR = len(grid)
        nC = len(grid[0])

        for rx in range(1, nR, 1):
            grid[rx][0] += grid[rx - 1][0]

        for cx in range(1, nC, 1):
            grid[0][cx] += grid[0][cx - 1]
        
        for rx in range(1, nR, 1):
            for cx in range(1, nC, 1):
                grid[rx][cx] += min(grid[rx - 1][cx], grid[rx][cx - 1])
        
        return grid[nR - 1][nC - 1]