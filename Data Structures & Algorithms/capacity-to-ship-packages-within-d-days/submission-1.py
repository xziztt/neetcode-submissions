class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def canShipWithinDays(weights,capacity,days):
            currDays = 1
            currWeight = 0
            for i in weights:
                if currWeight + i > capacity:
                    currWeight = 0
                    currDays += 1
                
                currWeight += i
            
            return currDays <= days
        

        left, right = max(weights), sum(weights)
        minCapacity = sum(weights)

        while left <= right:
            mid = left + (right - left)//2
            if canShipWithinDays(weights,mid,days):
                right = mid - 1
                minCapacity = min(minCapacity,mid)
            else:
                left = mid + 1
        
        return minCapacity

