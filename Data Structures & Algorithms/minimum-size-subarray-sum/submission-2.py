class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        right = 0
        currSum = 0
        minSubArray = len(nums) + 1

        while left <= right and right < len(nums):
            currSum += nums[right]


            while currSum >= target and left <= right:
                minSubArray = min(minSubArray, right - left + 1)
                currSum -= nums[left]
                left += 1
            
            right += 1
        

        if minSubArray == len(nums) + 1:
            return 0
        
        return minSubArray