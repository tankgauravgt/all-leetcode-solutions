from collections import Counter

class Solution:
    
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        wn = len(words)
        ws = len(words[0])
        
        N = len(s)
        tgt = dict(Counter(words))
        
        out = []
        for offset in range(ws):
            for ix in range(offset, N - (ws * wn) + 1, ws):
                src = [s[ix + jx:ix + jx + ws] for jx in range(0, (ws * wn), ws)]
                src = dict(Counter(src))
                if src == tgt:
                    out.append(ix)
        
        return out