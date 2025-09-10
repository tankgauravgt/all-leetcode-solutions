class Solution:
    def numDecodings(self, s: str) -> int:
        
        lookup = {
            '0': [],
            '1': ['1', *map(str, range(10, 20, 1))],
            '2': ['2', *map(str, range(20, 27, 1))],
            **{str(ix): [str(ix)] for ix in range(3, 10, 1)}
        }

        @cache
        def rec(sx):
            if sx >= len(s):
                return sx == len(s)
            count = 0
            for ss in lookup[s[sx]]:
                if s[sx:sx + len(ss)] == ss:
                    count = count + rec(sx + len(ss))
            return count
        
        return rec(0)