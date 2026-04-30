class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        minLength = len(nums) + 1
        left = 0
        right = 0
        currSum = 0
        while left <= right and right < len(nums):
            currSum += nums[right]
            
            while currSum >= target:
                minLength = min(minLength,right-left + 1)
                currSum -= nums[left]
                left += 1

                print("looping")
            
            right +=1
                

        if minLength == len(nums) + 1:
            return 0        
    
        return minLength

            
            