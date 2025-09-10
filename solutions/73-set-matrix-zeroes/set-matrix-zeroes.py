class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        nR = len(matrix)
        nC = len(matrix[0])
        
        frz = False
        fcz = False
        for rx in range(nR):
            fcz = fcz or (matrix[rx][0] == 0)
        for cx in range(nC):
            frz = frz or (matrix[0][cx] == 0)
        
        for rx in range(1, nR, 1):
            for cx in range(1, nC, 1):
                if matrix[rx][cx] == 0:
                    matrix[0][cx] = 0
                    matrix[rx][0] = 0

        for rx in range(1, nR):
            if matrix[rx][0] == 0:
                for cx in range(1, nC, 1):
                    matrix[rx][cx] = 0

        for cx in range(1, nC):
            if matrix[0][cx] == 0:
                for rx in range(1, nR, 1):
                    matrix[rx][cx] = 0

        if frz == True:
            for cx in range(nC):
                matrix[0][cx] = 0

        if fcz == True:
            for rx in range(nR):
                matrix[rx][0] = 0
