from collections import Counter

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        N = len(nums)

        src = dict(Counter(nums))
        tgt = {}

        def rec(buf, res):
            nonlocal src, tgt
            if len(buf) == N:
                res.append(buf.copy())
                return
            for n in src:
                if tgt.get(n, 0) < src.get(n, 0):
                    tgt[n] = tgt.get(n, 0) + 1
                    buf.append(n)
                    rec(buf, res)
                    buf.pop()
                    tgt[n] = tgt.get(n, 0) - 1
        
        result = []
        rec([], result)
        return result