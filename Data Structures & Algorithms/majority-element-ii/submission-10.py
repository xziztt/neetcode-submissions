class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        if len(nums) ==0:
            return []
        elif len(nums) == 1:
            return [nums[0]]
        elementOne = None
        elementTwo = None

        freqOne = 0
        freqTwo = 0

        for i in range(0,len(nums)):
            if nums[i] == elementOne:
                freqOne += 1
            elif nums[i] == elementTwo:
                freqTwo += 1
            elif freqOne == 0:
                freqOne = 1
                elementOne = nums[i]
            elif freqTwo == 0:
                freqTwo  = 1
                elementTwo = nums[i]
            else:
                freqOne -=1
                freqTwo -= 1
                
        result = []
        if nums.count(elementOne) > len(nums)//3:
            result.append(elementOne)
        
        if elementOne != elementTwo and nums.count(elementTwo) > len(nums)// 3:
            result.append(elementTwo)

        return result