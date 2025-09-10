class Solution:
    def romanToInt(self, s: str) -> int:

        valmap = {
            'I': 1, 
            'IV': 4, 
            'V': 5, 
            'IX': 9, 
            'X': 10, 
            'XL': 40,
            'L': 50,
            'XC': 90,
            'C': 100,
            'CD': 400,
            'D': 500,
            'CM': 900,
            'M': 1000
        }

        lx = 0
        total = 0
        while lx < len(s):
            for pre in ['CM', 'CD', 'XC', 'XL', 'IX', 'IV']:
                if s[lx::].startswith(pre):
                    total = total + valmap[pre]
                    lx = lx + len(pre)
                    continue
            if lx < len(s):
                total = total + valmap[s[lx]]
                lx = lx + 1
        return total