class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        for sell_d in range(1,len(prices)):
            buy_min = min(prices[0:sell_d])
            profit = prices[sell_d] - buy_min
            if profit > max_profit:
                max_profit = profit
        return max_profit