class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:

        buf = []
        res = []
        vrec = set()

        def rec(sx):
            nonlocal buf, res, vrec
            if len(buf) == k:
                res.append(buf.copy())
                return
            for ix in range(sx, 1 + n):
                if ix not in vrec:
                    vrec.add(ix)
                    buf.append(ix)
                    rec(1 + ix)
                    buf.pop()
                    vrec.remove(ix)
        
        rec(1)
        return res