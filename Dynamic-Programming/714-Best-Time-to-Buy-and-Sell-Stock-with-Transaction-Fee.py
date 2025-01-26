class Solution:
    def maxProfit(self, prices: list[int], fee: int) -> int:
        buy = float("-inf")
        sell = 0

        # States: hold, sold, bought
        for p in prices:
            buy = max(buy, sell - p)
            sell = max(sell, buy + p - fee)

        return sell