class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        nR = len(matrix)
        nC = len(matrix[0])

        row = list(map(int, matrix[0].copy()))

        def rect_area(arr):
            tmp = [0] + arr + [0]
            out = 0
            stk = []
            for hx, h in enumerate(tmp):
                while stk and tmp[stk[-1]] > h:
                    hh = tmp[stk.pop()]
                    ww = (hx - 1) - stk[-1]
                    out = max(out, ww * hh)
                stk.append(hx)
            return out

        cmax = rect_area(row)
        for rx in range(1, nR, 1):
            for cx in range(nC):
                if matrix[rx][cx] == "0":
                    row[cx] = 0
                else:
                    row[cx] += 1
            cmax = max(cmax, rect_area(row))
        
        return cmax