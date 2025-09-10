class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        def top(mat, sr, er, sc, ec):
            out = []
            for cx in range(sc, 1 + ec, +1):
                out.append(mat[sr][cx])
            return out
        def right(mat, sr, er, sc, ec):
            out = []
            for rx in range(sr, 1 + er, +1):
                out.append(mat[rx][ec])
            return out
        def bottom(mat, sr, er, sc, ec):
            out = []
            for cx in range(ec, sc - 1, -1):
                out.append(mat[er][cx])
            return out
        def left(mat, sr, er, sc, ec):
            out = []
            for rx in range(er, sr - 1, -1):
                out.append(mat[rx][sc])
            return out
        
        init_r, init_c = 0, 0
        stop_r, stop_c = len(matrix) - 1, len(matrix[0]) - 1

        ctr = 0
        result = []
        TOTAL_LIMIT = len(matrix) * len(matrix[0])
        while init_r <= stop_r and init_c <= stop_c:
            if ctr < TOTAL_LIMIT and init_c <= stop_c:
                temp = top(matrix, init_r, stop_r, init_c, stop_c)
                result.extend(temp)
                ctr = ctr + len(temp)
                init_r = init_r + 1
            if ctr < TOTAL_LIMIT and init_r <= stop_r:
                temp = right(matrix, init_r, stop_r, init_c, stop_c)
                result.extend(temp)
                ctr = ctr + len(temp)
                stop_c = stop_c - 1
            if ctr < TOTAL_LIMIT and init_c <= stop_c:
                temp = bottom(matrix, init_r, stop_r, init_c, stop_c)
                result.extend(temp)
                ctr = ctr + len(temp)
                stop_r = stop_r - 1
            if ctr < TOTAL_LIMIT and init_r <= stop_r:
                temp = left(matrix, init_r, stop_r, init_c, stop_c)
                result.extend(temp)
                ctr = ctr + len(temp)
                init_c = init_c + 1
            if ctr == TOTAL_LIMIT:
                break
        return result