class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        
        int_min = -(2 ** 31)
        int_max = +(2 ** 31) - 1

        a, b = dividend, divisor

        if a == int_min and b == -1:
            return int_max
        
        sign = (a < 0) ^ (b < 0)
        a = abs(a)
        b = abs(b)

        total = 0
        for ix in range(31, -1, -1):
            if a >= (b << ix):
                a = a - (b << ix)
                total = total + (1 << ix)
        
        return total if not sign else -total