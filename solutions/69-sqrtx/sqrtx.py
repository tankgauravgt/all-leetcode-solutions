class Solution:
    def mySqrt(self, x: int) -> int:
        
        lx = 0
        rx = x

        for ix in range(100):
            mx = lx + (rx - lx) / 2
            if mx * mx < x:
                lx = mx
            else:
                rx = mx
        
        return int(mx)