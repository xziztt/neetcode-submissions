class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        curr_max = nums[0]
        curr_val = 0

        for i in nums:
            if curr_val < 0:
                curr_val = 0
                curr_max = i
            
            if curr_max == i:
                curr_val += 1
            else:
                curr_val -= 1
        
        return curr_max
            