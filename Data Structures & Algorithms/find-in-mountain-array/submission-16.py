class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        
        def findInAsc(target, left, right):
            
            while left <= right:
                mid = left + (right - left)//2
                val = mountainArr.get(mid)
                if val == target:
                    return mid
                elif val > target:
                    right = mid - 1
                else:
                    left = mid + 1
            return -1
        
        def findInDesc(target, left, right):
            while left <= right:
                mid = left + (right - left)//2
                val = mountainArr.get(mid)
                if val == target:
                    return mid
                elif val > target:
                    left = mid + 1
                else:
                    right = mid - 1
            return - 1

        lenArr = mountainArr.length()

        left, right = 0, lenArr - 1

        while left < right:
            mid = left + (right - left)//2
            val = mountainArr.get(mid)
            if val < mountainArr.get(mid + 1):
               left = mid + 1
            else:
                right = mid

        peak = left

        val = findInAsc(target,0,peak)
        if val != -1:
            return val

        return findInDesc(target,peak + 1,lenArr - 1)
        
