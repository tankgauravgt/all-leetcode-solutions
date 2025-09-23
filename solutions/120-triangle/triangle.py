class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:

        nR = len(triangle)
        for rx in range(nR - 2, -1, -1):
            nC = len(triangle[rx])
            for cx in range(nC):
                triangle[rx][cx] += min(triangle[rx + 1][cx], triangle[rx + 1][cx + 1])
        
        return triangle[0][0]