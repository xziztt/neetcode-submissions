class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        currProfit = 0
        currMaxProfit = 0
        currMinElement = prices[0]
        for i in range(0,len(prices)):
            currMinElement = min(currMinElement,prices[i])
            currProfit = prices[i] - currMinElement
            if currProfit < 0:
                currProfit = 0
                continue
            currMaxProfit = max(currMaxProfit,currProfit)
        
        return currMaxProfit