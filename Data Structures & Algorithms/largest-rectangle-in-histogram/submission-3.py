class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        stack = []
        maxArea = 0
        
        heights.append(0)
        
        for i in range(len(heights)):
            while stack and heights[i] < heights[stack[-1]]:
                currIndex = stack.pop()
                leftIndex = 0 
                if stack:
                    leftIndex = stack[-1] + 1
                
                rightIndex = i - 1

                width = rightIndex - leftIndex + 1

                area = heights[currIndex] * width

                maxArea = max(maxArea,area)
            
            stack.append(i)
        

        return maxArea
