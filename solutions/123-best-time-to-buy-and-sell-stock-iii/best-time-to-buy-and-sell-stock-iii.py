from functools import cache
from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        Calculates the maximum profit with at most two transactions.

        This solution uses a recursive approach with memoization (via @cache).
        The state is defined by (day_index, transaction_id), where:
        - day_index: The current day we are considering (from 0 to N-1).
        - transaction_id: The current action number (0 to 3).
          - 0: First Buy
          - 1: First Sell
          - 2: Second Buy
          - 3: Second Sell
        
        If transaction_id is even, we are in a 'buy' state.
        If transaction_id is odd, we are in a 'sell' state.
        """
        N = len(prices)
        
        # The number of allowed transactions is 2, which means 4 operations total.
        MAX_TRANSACTIONS = 4

        @cache
        def solve(day_index: int, transaction_id: int) -> int:
            # Base Case 1: If we have run out of days, no more profit can be made.
            # Base Case 2: If we have completed all allowed transactions.
            if day_index == N or transaction_id == MAX_TRANSACTIONS:
                return 0

            # --- Decision 1: Do nothing today ---
            # We skip the current day and see what profit we can make from tomorrow
            # with the same transaction state.
            do_nothing_profit = solve(day_index + 1, transaction_id)
            
            # --- Decision 2: Act today (Buy or Sell) ---
            if transaction_id % 2 == 0:  # We are in a 'buy' state
                # We buy the stock, which costs us money (-prices[day_index]).
                # Then, we move to the next day and the next transaction state (a 'sell' state).
                action_profit = -prices[day_index] + solve(day_index + 1, transaction_id + 1)
            else:  # We are in a 'sell' state
                # We sell the stock, which makes us money (+prices[day_index]).
                # Then, we move to the next day and the next transaction state (a 'buy' state).
                action_profit = prices[day_index] + solve(day_index + 1, transaction_id + 1)
            
            # The result for the current state is the maximum of the two decisions.
            return max(do_nothing_profit, action_profit)

        # Start the process on day 0, in the state for the first transaction (buy).
        return solve(0, 0)