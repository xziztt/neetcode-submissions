class Solution:
    
    def reverse_list(self, nums: List[int], start: int, end: int):
        while start <= end:
            nums[start],nums[end] = nums[end], nums[start]
            start += 1
            end -= 1
    
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k%len(nums)
        nums.reverse()
        self.reverse_list(nums,0,k-1)
        self.reverse_list(nums,k,len(nums) - 1)

        