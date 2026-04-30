class Solution:
    
    def splitArray(self, nums: List[int], k: int) -> int:
        

        def canSplit(nums,k,currMin):
            currSum = 0
            currSplits = 1

            for i in nums:
                if currSum + i > currMin:
                    currSplits += 1
                    currSum = 0
                currSum += i   

            return currSplits <= k 


        left, right = max(nums), sum(nums)
        minSplit = sum(nums)
        while left <= right:
            mid = left + (right - left)//2

            if canSplit(nums,k,mid):
                minSplit = min(minSplit,mid)
                right = mid - 1
            else:
                left = mid + 1
        
        return minSplit