import math

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        m = matrix
        
        nR = len(matrix)
        nC = len(matrix[0])

        def swap_element(m, rx, cx):
            # ++, +-, --, -+
            temp1 = m[rx][cx]
            temp2 = m[cx][nR - 1 - rx]
            temp3 = m[nR - 1 - rx][nC - 1 - cx]
            temp4 = m[nC - 1 - cx][rx]
            m[cx][nR - 1 - rx] = temp1
            m[nR - 1 - rx][nC - 1 - cx] = temp2
            m[nC - 1 - cx][rx] = temp3
            m[rx][cx] = temp4

        for rx in range(math.floor(nR / 2)):
            for cx in range(math.ceil(nC / 2)):
                swap_element(m, rx, cx)