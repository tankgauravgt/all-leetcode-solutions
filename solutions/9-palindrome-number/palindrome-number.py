class Solution:
    def isPalindrome(self, x: int) -> bool:
        s = str(x)
        
        lx = 0
        rx = len(s) - 1
        while lx < rx and s[lx] == s[rx]:
            lx = lx + 1
            rx = rx - 1
        
        return lx >= rx