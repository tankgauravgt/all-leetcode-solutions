class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        N = len(prices)

        @cache
        def rec(sx, n_tx):
            if sx == N or n_tx == 2 * k:
                return 0
            return max(
                rec(1 + sx, n_tx),
                (2 * (n_tx % 2) - 1) * prices[sx] + rec(1 + sx, n_tx + 1)
            )
        
        return rec(0, 0)