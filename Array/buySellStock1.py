class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minprice = 10**6
        profit = 0
        for i in range(len(prices)):
            if prices[i] < minprice:
                minprice = prices[i]
            elif (prices[i] - minprice > 0) and (prices[i] - minprice > profit):
                profit = prices[i] - minprice
        return profit