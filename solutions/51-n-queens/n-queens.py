class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        
        M = [['.'] * n for ix in range(n)]

        def is_collision(mat, rx, cx):
            nR, nC = len(mat), len(mat[0])
            for r in range(0, nR):
                if r == rx: continue
                if mat[r][cx] == 'Q': return True
            for c in range(0, nC):
                if c == cx: continue
                if mat[rx][c] == 'Q': return True
            for d in range(-nR, nR):
                r, c = rx + d, cx + d
                if 0 <= r < nR and 0 <= c < nC:
                    if mat[r][c] == 'Q': return True
            for d in range(-nR, nR):
                r, c = rx + d, cx - d
                if 0 <= r < nR and 0 <= c < nC:
                    if mat[r][c] == 'Q': return True
            return False

        blacklist_col = set()
        def btrack(mat, rx, rem, res):
            nR, nC = len(mat), len(mat[0])
            if rem == 0:
                return res.append(["".join(row) for row in mat])
            for cx in range(nC):
                if cx in blacklist_col:
                    continue
                if mat[rx][cx] == '.' and not is_collision(mat, rx, cx):
                    mat[rx][cx] = 'Q'
                    blacklist_col.add(cx)
                    btrack(mat, 1 + rx, rem - 1, res)
                    blacklist_col.remove(cx)
                    mat[rx][cx] = '.'
            return False
        
        res = []
        btrack(M, 0, n, res)
        return res