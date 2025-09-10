class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        lx = 0
        rec = {}

        cmax = 0
        for rx, c in enumerate(s):
            
            # look in current receptive field only. 
            # i.e., condition: `rec[c] >= lx`
            # -------------------------------
            if c in rec and rec[c] >= lx:
                lx = rec[c] + 1
            
            rec[c] = rx
            cmax = max(cmax, rx - lx + 1)
        
        return cmax