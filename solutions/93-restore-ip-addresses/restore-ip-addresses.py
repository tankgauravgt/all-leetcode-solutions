class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        
        possible = set([str(ix) for ix in range(256)])
        
        def valid(s):
            for nstr in s.split('.'):
                if nstr not in possible:
                    return False
            return True

        def rec(sx, buf, res):
            if buf.count('.') > 3:
                return
            if len(buf) > len(s) + 3:
                return
            if sx == len(s):
                if buf.count('.') == 3:
                    if valid(buf):
                        res.append(buf)
                return
            rec(1 + sx, buf + s[sx], res)
            if buf and buf[-1] != '.':
                rec(sx, buf + '.', res)

        result = []
        rec(0, '', result)
        return result