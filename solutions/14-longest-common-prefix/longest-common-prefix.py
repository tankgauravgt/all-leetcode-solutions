class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        smin = min(strs, key=len)
        for ix, c in enumerate(smin):
            if len(set([s[ix] for s in strs])) != 1:
                return smin[:ix]
        return smin