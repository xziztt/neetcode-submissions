class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        currProfit = 0
        currMin = prices[0]
        for i in range(1,len(prices)):
            print(currMin,prices[i],prices[i] - currMin)
            if prices[i] - currMin < 0:
                currMin = prices[i]
                continue
            currProfit += prices[i] - currMin 
            currMin = prices[i]
        
        return currProfit