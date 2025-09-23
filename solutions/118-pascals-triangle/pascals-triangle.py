class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        out = [[1]]
        for n in range(numRows - 1):
            out.append([1])
            for ix, nn in enumerate(out[-2]):
                if ix == 0:
                    continue
                out[-1].append(nn + out[-2][ix - 1])
            out[-1].append(1)
        return out