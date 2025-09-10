class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        N = len(candidates)

        candidates.sort()

        buf = []
        out = []
        def comb(sx, rem):
            if sx == N:
                if rem == 0:
                    out.append(buf.copy())
                return
            if rem >= candidates[sx]:
                buf.append(candidates[sx])
                comb(sx + 1, rem - candidates[sx])
                buf.pop()
            ix = sx
            while ix < N - 1 and candidates[ix] == candidates[ix + 1]:
                ix = ix + 1
            comb(ix + 1, rem)
        
        comb(0, target)
        return out