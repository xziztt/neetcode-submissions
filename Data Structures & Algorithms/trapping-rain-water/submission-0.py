class Solution:
    def trap(self, height: List[int]) -> int:
        i = 0
        j = len(height) - 1
        maxLeft = height[0]
        maxRight = height[j]
        area = 0
        while i < j:
            maxLeft = max(height[i],maxLeft)
            maxRight = max(height[j],maxRight)

            if height[i] < height[j]:
                area += min(maxLeft,maxRight) - height[i]
                i+=1
                print("moving right", area)
            else:
                area+= min(maxLeft,maxRight) - height[j]
                j-=1

                print("moving left", area)

        return area