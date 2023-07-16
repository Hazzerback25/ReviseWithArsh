class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        low=prices[0]
        profit=0
        for i in range(len(prices)):
            diff=prices[i]-low
            profit=max(profit,diff)
            low=min(prices[i],low)
        return(profit)
