class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        nR = len(matrix)
        nC = len(matrix[0])

        def binsearch(lx, rx, tgt):
            if lx <= rx:
                mx = lx + (rx - lx) // 2
                if matrix[mx // nC][mx % nC] < target:
                    return binsearch(mx + 1, rx, tgt)
                elif matrix[mx // nC][mx % nC] > target:
                    return binsearch(lx, mx - 1, tgt)
                else:
                    return True
            return False
        
        return binsearch(0, nR * nC - 1, target)