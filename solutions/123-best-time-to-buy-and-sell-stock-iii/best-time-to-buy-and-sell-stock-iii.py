from functools import cache
from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        N = len(prices)

        MAX_TRANSACTIONS = 4

        @cache
        def solve(day_index: int, transaction_id: int) -> int:
            if day_index == N or transaction_id == MAX_TRANSACTIONS:
                return 0
            
            do_nothing_profit = solve(day_index + 1, transaction_id)
            
            if transaction_id % 2 == 0:
                action_profit = -prices[day_index] + solve(day_index + 1, transaction_id + 1)
            else:
                action_profit = prices[day_index] + solve(day_index + 1, transaction_id + 1)
            
            return max(do_nothing_profit, action_profit)

        return solve(0, 0)