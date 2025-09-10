class Solution:
    def reverse(self, x: int) -> int:
        
        # record the sign
        sign = -1 if x < 0 else +1

        # set limits without overflowing the values
        limit = 2 ** 30 + ((2 ** 30) - 1) if sign == +1 else 2 ** 31

        x = abs(x)

        cnum = 0
        while x:
            
            # look ahead if overflow can happen
            if cnum > limit // 10:
                return 0
            
            # corner case for overflow comparing last digit
            if cnum == limit // 10 and (x % 10 > limit % 10):
                return 0
            
            # update the value:
            cnum = cnum * 10 + (x % 10)
            x = x // 10
        
        return sign * cnum