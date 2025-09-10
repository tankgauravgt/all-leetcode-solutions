class Solution:
    def isValid(self, s: str) -> bool:
        
        comp = {
            ')': '(',
            '}': '{',
            ']': '['
        }
        
        stk = []
        for cx, c in enumerate(s):
            if not stk and c in ')}]':
                return False
            if stk and c in ')}]':
                if comp[c] != stk[-1]:
                    return False
                stk.pop()
                continue
            stk.append(c)
        
        return len(stk) == 0