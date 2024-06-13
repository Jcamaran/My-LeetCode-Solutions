class Solution(object):
    def maxProfit(self, prices):
        buy_price = prices[0]
        profit = 0
        for p in prices[1:]:
            if buy_price > p:
                buy_price = p
            
            profit = max(profit, p - buy_price)
        
        return profit
