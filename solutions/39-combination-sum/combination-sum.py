class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        N = len(candidates)

        buf = []
        out = []
        def comb(sx, rem):
            if sx == N:
                if rem == 0:
                    out.append(buf.copy())
                return
            if rem >= candidates[sx]:
                buf.append(candidates[sx])
                comb(sx, rem - candidates[sx])
                buf.pop()
            comb(sx + 1, rem)
        
        comb(0, target)
        return out