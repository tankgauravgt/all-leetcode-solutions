class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        
        out = [1]
        for n in range(rowIndex):
            temp = []
            N = len(out)
            temp.append(1)
            for ix in range(1, N):
                temp.append(out[ix - 1] + out[ix])
            temp.append(1)
            out = temp
        
        return out