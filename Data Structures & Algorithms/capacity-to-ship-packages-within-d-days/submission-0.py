class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        
        left, right = max(weights), sum(weights)

        def canShip(weights,allowedWeight,days):
            currDays = 1
            currWeight = 0
            for i in weights:
                if currWeight + i > allowedWeight:
                    currDays += 1
                    currWeight = 0
                currWeight += i
            
            return currDays <= days


        minDays = days

        while left <= right:
            mid = left + (right-left)//2

            if canShip(weights,mid,days):
                minDays = min(mid, minDays)
                right = mid - 1
            else:
                left = mid + 1
            
        
        return left
            


