class Solution:
    def isNumber(self, s: str) -> bool:
        
        s.lstrip('0')
        parts = s.split('e')
        
        def parseInt(string):
            if not string: False
            try:
                eval(f"int('{string}')")
                return True
            except:
                return False
        
        def parseFloat(string):
            skipwords = [
                'nan', 'inf', '-inf', '+inf',
                'Infinity', '-Infinity', '+Infinity'
            ]
            if not string: return False
            if string in skipwords: return False
            try:
                eval(f"float('{string}')")
                return True
            except:
                return False


        if len(parts) == 1:
            return parseFloat(parts[0])
        
        if len(parts) == 2:
            return parseFloat(parts[0]) and parseInt(parts[1])
        
        return False