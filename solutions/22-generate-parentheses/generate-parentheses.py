class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        def rec(o, c, buf, res):
            if o + c == 2 * n:
                res.append(''.join(buf))
                return
            
            # =====================
            # allow for 0 to n - 1:
            # =====================

            if o < n:
                buf.append('(')
                rec(o + 1, c, buf, res)
                buf.pop()
            
            if o > c:
                buf.append(')')
                rec(o, c + 1, buf, res)
                buf.pop()
        
        result = []
        rec(0, 0, [], result)
        return result