class Solution:
    def mySqrt(self, x: int) -> int:
        left, right = 1, x//2
        result = 0

        if x < 2:
            return x

        while left <= right:
            mid = left + (right - left)//2
            val  = mid * mid

            if x == val:
                return mid
            elif val < x:
                result = mid
                left = mid + 1
            else:
                right = mid - 1

        return result