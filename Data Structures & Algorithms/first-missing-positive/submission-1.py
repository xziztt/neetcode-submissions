class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        
        for i in range(0,len(nums)):
            while 1 <= nums[i] <= len(nums) and nums[nums[i] - 1] != nums[i]:
                newIndex = nums[i] - 1
                nums[newIndex],nums[i] = nums[i],nums[newIndex]
            
        
        for i in range(0,len(nums)):
            if nums[i] != i + 1:
                return i + 1
            
        

        return nums[len(nums) - 1] + 1