class Solution:
    def grayCode(self, n: int) -> List[int]:
        
        out = [[0], [1]]
        while n - 1:
            tmp = []
            for b in [0, 1]:
                if b == 0:
                    for ix in range(len(out)):
                        tmp.append(out[ix].copy())
                        tmp[-1].append(b)
                else:
                    for ix in range(len(out) - 1, -1, -1):
                        tmp.append(out[ix].copy())
                        tmp[-1].append(b)
            out = tmp
            n = n - 1
        
        return [int("".join(map(str, arr))[::-1], 2) for arr in out]