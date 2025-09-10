class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        @cache
        def dnc(x, p):
            if p == 0:
                return 1
            if p == 1:
                return x
            return dnc(x, p // 2) * dnc(x, p // 2) * (x if (p % 2) else 1)
        
        if n < 0:
            return 1 / dnc(x, -n)
        return dnc(x, n)