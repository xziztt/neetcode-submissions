class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        def getBananaEatingHours(piles,rate,h):
            currHours = 0
            for i in piles:
                currHours += math.ceil(i/rate)
            return currHours

        left, right = 1, max(piles)
        minRate = max(piles)
        piles.sort()

        while left <= right:
            rate = left + (right-left)//2
            bananaEatingHours =  getBananaEatingHours(piles,rate,h)
            if bananaEatingHours <= h:
                minRate = min(rate,minRate)
                right = rate - 1
            else:
                left = rate + 1
        
        return minRate
            