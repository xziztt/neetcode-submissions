class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        maxList = []

        left = 0
        right = k - 1

        while left <= right and right < len(nums):
            maxList.append(max(nums[left:right + 1]))
            left+=1
            right +=1
        
        return maxList