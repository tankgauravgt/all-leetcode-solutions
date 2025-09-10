class Solution:
    def intToRoman(self, num: int) -> str:
        
        keys = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        vals = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']

        cache = dict(zip(keys, vals))

        out = []
        ix = 0
        while num:
            while num < keys[ix]:
                ix = ix + 1
            num = num - keys[ix]
            out.append(vals[ix])
        return "".join(out)