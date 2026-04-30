from collections import deque

class Solution:

    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq = deque()
        maxElements = []
        for i in range(len(nums)):

            while dq and nums[dq[-1]] < nums[i]:
                dq.pop()
        
            
            if dq and dq[0] < i - k + 1:
                dq.popleft()


            dq.append(i)

            if dq and i >= k-1:
                maxElements.append(nums[dq[0]])
            
        
        return maxElements

