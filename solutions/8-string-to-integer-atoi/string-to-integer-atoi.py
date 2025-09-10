class Solution:
    def myAtoi(self, s: str) -> int:

        ix = 0
        N = len(s)
        
        # remove whitespaces
        while ix < N and s[ix] == ' ':
            ix = ix + 1
        
        sign = +1

        # infer sign
        if ix < N and s[ix] in {'+', '-'}:
            sign = (+1 if s[ix] == '+' else -1)
            ix = ix + 1
        
        # read max non-digits
        out = 0
        while ix < N:
            if not s[ix].isdigit():
                break
            out = out * 10 + int(s[ix])
            ix = ix + 1
        
        # clamp and return number
        return min(max(sign * out, -(2 ** 31)), (2 ** 31) - 1)