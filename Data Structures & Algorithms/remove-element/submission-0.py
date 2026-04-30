class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        curr_end = len(nums) - 1
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] == val:
                nums[i], nums[curr_end] = nums[curr_end],nums[i]
                curr_end -= 1
        
        return curr_end + 1

