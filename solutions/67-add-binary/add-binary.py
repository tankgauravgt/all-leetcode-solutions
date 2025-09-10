class Solution:
    def addBinary(self, a: str, b: str) -> str:
        
        a = list(a)
        b = list(b)

        c = 0
        out = []
        while a or b:
            
            b1 = 0 if not a else a.pop()
            b2 = 0 if not b else b.pop()

            out.append(c + int(b1) + int(b2))
            
            c = out[-1] // 2
            out[-1] = out[-1] % 2

        if c:
            out.append(c)
        
        return "".join(list(map(str, out))[::-1])