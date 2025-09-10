class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        cache = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        def rec(dx, buf, res):
            if dx == len(digits):
                if buf:
                    res.append("".join(buf))
                return
            for c in cache[digits[dx]]:
                buf.append(c)
                rec(dx + 1, buf, res)
                buf.pop()
        
        out = []
        rec(0, [], out)
        return out