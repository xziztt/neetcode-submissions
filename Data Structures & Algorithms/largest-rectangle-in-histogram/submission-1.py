class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        heights.append(0)
        maxArea = 0
        for i in range(len(heights)):
            while stack and heights[i] < heights[stack[-1]]:
                currHeightIndex = stack.pop()
                currHeight = heights[currHeightIndex]

                leftIndex = 0 if not stack else (stack[-1] + 1)
                
                width = (i - 1) - (leftIndex) + 1

                print(width)

                area = currHeight * width
                maxArea = max(maxArea,area)
            stack.append(i)

        
        return maxArea