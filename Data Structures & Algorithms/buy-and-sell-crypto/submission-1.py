class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_buy = prices[0]
        for sell_d in range(1,len(prices)):
            min_buy = min(min_buy, prices[sell_d])
            profit = prices[sell_d] - min_buy
            if profit > max_profit:
                max_profit = profit
        return max_profit