class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_buy = prices[0]
        for sell in prices:
            min_buy = min(min_buy, sell)
            profit = sell - min_buy
            if profit > max_profit:
                max_profit = profit
        return max_profit