class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:

        init_rx = 0
        init_cx = 0
        stop_rx = n - 1
        stop_cx = n - 1

        mat = []
        for ix in range(n):
            mat.append([0 for jx in range(n)])

        count = 0
        while count < (n * n):
            
            if count < (n * n):
                for cx in range(init_cx, stop_cx + 1, +1):
                    mat[init_rx][cx] = count + 1
                    count = count + 1
                init_rx = init_rx + 1
            
            if count < (n * n):
                for rx in range(init_rx, stop_rx + 1, +1):
                    mat[rx][stop_cx] = count + 1
                    count = count + 1
                stop_cx = stop_cx - 1
            
            if count < (n * n):
                for cx in range(stop_cx, init_cx - 1, -1):
                    mat[stop_rx][cx] = count + 1
                    count = count + 1
                stop_rx = stop_rx - 1
            
            if count < (n * n):
                for rx in range(stop_rx, init_rx - 1, -1):
                    mat[rx][init_cx] = count + 1
                    count = count + 1
                init_cx = init_cx + 1
        
        return mat