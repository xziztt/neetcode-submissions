class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
            hashMap = {}

            for i in range(0, len(nums)):
                if nums[i] not in hashMap.keys():
                    hashMap[nums[i]] = i
                else:
                    prevIndex = hashMap[nums[i]]
                    if abs(prevIndex - i) <= k:
                        return True
                    hashMap[nums[i]] = i
            
            return False