class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        finalList = []
        nums.sort()
        for i in range(0,len(nums) - 2):
            if i > 0 and nums[i] == nums[i-1]:
                continue

            left, right = i+1,  len(nums)-1

            while left < right:
                total = nums[i] + nums[left] + nums[right]

                # print("total, i, left, right",total,i,left,right)
                if total == 0:
                    finalList.append([nums[i],nums[left],nums[right]])

                    while left < right and nums[left] == nums[left+1]:
                        left += 1
                    while left < right and nums[right] == nums[right-1]:
                        right -= 1

                    left += 1
                    right -=1

                else:
                    if total < 0:
                        left += 1
                    else:
                        right -=1

        

        return finalList

                    