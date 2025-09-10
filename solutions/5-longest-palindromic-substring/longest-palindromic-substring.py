class Solution:
    def longestPalindrome(self, s: str) -> str:
        N = len(s)
        cmax = 0
        output = ""
        for ix in range(N):
            lx = rx = ix
            while lx >= 0 and rx < N and s[lx] == s[rx]:
                if cmax < rx - lx + 1:
                    output = s[lx:1 + rx]
                    cmax = rx - lx + 1
                lx = lx - 1
                rx = rx + 1
        for ix in range(N - 1):
            lx = ix
            rx = ix + 1
            while lx >= 0 and rx < N and s[lx] == s[rx]:
                if cmax < rx - lx + 1:
                    output = s[lx:1 + rx]
                    cmax = rx - lx + 1
                lx = lx - 1
                rx = rx + 1        
        return output