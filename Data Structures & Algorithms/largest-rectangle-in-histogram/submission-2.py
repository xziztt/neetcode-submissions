class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        heights.append(0)
        maxArea = 0

        for i in range(0,len(heights)):
    
            while stack and heights[i] < heights[stack[-1]]:
                currIndex = stack.pop()
                currHeight = heights[currIndex]
                rightIndex = i
                leftIndex = 0
                if stack:
                    leftIndex = stack[-1] + 1

                width = (rightIndex - 1) - leftIndex + 1

                maxArea = max(maxArea,currHeight * width)
            
            stack.append(i)

        return maxArea