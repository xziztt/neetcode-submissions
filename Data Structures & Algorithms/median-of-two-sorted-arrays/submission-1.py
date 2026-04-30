class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        m = len(nums1)
        n = len(nums2)

        if m > n:
            nums1, nums2 = nums2, nums1
            m,n = n,m
        
        totalLenLeft = (m + n + 1)//2
        left = 0
        right = m

        while left <= right:
            partition1 = left + (right - left)//2
            partition2 = totalLenLeft - partition1


            maxLeft1 = float('-inf') if partition1 == 0 else nums1[partition1 - 1]
            minRight1 = float('inf') if partition1 == m else nums1[partition1]

            maxLeft2 = float('-inf') if partition2 == 0 else nums2[partition2 - 1]
            minRight2 = float('inf') if partition2 == n else nums2[partition2] 


            if maxLeft1 <= minRight2 and maxLeft2 <= minRight1:
                if (m + n) % 2 == 0:
                    return (max(maxLeft1,maxLeft2) + min(minRight1,minRight2))/2
                else:
                    return max(maxLeft1,maxLeft2)
            elif maxLeft1 > minRight2:
            # We're too far right in nums1
                right = partition1 - 1
            else:
            # We're too far left in nums1
                left = partition1 + 1

        return 0