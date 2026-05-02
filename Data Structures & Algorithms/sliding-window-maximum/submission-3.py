from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq = deque()

        left = 0
        right = 0
        results = []

        while right < len(nums):

            while dq and nums[dq[-1]] < nums[right]:
                dq.pop()
            
            if dq and dq[0] < right - k + 1:
                dq.popleft()

            

            dq.append(right)

            if dq and right >= k - 1:
                results.append(nums[dq[0]])
            
            right += 1            
            
        
        return results
