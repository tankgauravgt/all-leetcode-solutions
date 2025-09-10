from collections import defaultdict

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows == len(s):
            return s
        
        px = 0
        rev = True
        cache = defaultdict(list)
        for ix, c in enumerate(s):
            if px == 0 or px == numRows - 1:
                rev = not rev
            cache[px].append(c)
            px = px + (1 if not rev else -1)
        
        return "".join(["".join(arr) for arr in cache.values()])