class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hashMap = {}
        left = 0
        right = len(nums) - 1

        while left <= right:
            if nums[left] not in hashMap.keys():
                hashMap[nums[left]] = left
            else:
                prevIndex = hashMap[nums[left]]
                print(nums[left])
                if abs(prevIndex - left) <= k:
                    return True
                hashMap[nums[left]] = left
            left += 1

        return False