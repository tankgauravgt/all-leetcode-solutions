class Solution:
    def maxSubArray(self, arr):
        csum = 0
        cmax = max(arr)
        for ix, n in enumerate(arr):
            csum = csum + n
            cmax = max(cmax, csum)
            if csum < 0:
                csum = 0
        return cmax