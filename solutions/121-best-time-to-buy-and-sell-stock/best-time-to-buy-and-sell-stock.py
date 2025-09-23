class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        N = len(prices)

        cmin = prices[0]
        
        pmax = 0
        for ix in range(1, N, 1):
            pmax = max(pmax, prices[ix] - cmin)
            cmin = min(cmin, prices[ix])
        
        return pmax