class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        currProfit = 0
        maxProfit = -1
        minVal = prices[0]
        for i in range(0,len(prices)):
            currProfit = prices[i] - minVal

            if currProfit < 0:
                currProfit = 0
            minVal = min(prices[i], minVal)
            maxProfit = max(currProfit, maxProfit)
        
        return maxProfit