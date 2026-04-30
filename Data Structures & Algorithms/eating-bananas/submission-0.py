import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        def getTotalTimeToEatBananas(piles, rate, h):
            totalTime = 0
            for i in piles:
                totalTime += math.ceil(i/rate)
            return totalTime

        piles.sort()
        left, right = 1, piles[-1]

        minTime = piles[-1]

        while left <= right:
            mid = left + (right - left)//2
            totalTimeToEatBananas = getTotalTimeToEatBananas(piles,mid,h)
            
            if totalTimeToEatBananas <= h:
                minTime = mid
                right = mid - 1
            else:
                left = mid + 1
        
        return minTime