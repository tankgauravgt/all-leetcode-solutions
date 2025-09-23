class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        N = len(prices)

        total = 0
        for ix in range(1, N):
            total += max(0, prices[ix] - prices[ix - 1])
        
        return total