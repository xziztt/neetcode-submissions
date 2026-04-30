class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        firstElement = None
        secondElement = None

        firstFreq = 0
        secondFreq = 0

        for i in nums:
            if i == firstElement:
                firstFreq += 1
            elif i == secondElement:
                secondFreq += 1
            elif firstFreq == 0:
                firstElement = i
                firstFreq = 1
            elif secondFreq == 0:
                secondElement = i
                secondFreq = 1
            else:
                firstFreq -= 1
                secondFreq -= 1

        result = []
        print(firstElement, secondElement)
        print(firstFreq,  secondFreq)
        if nums.count(firstElement) > len(nums)//3:
            result.append(firstElement)
        
        if secondElement!=firstElement and nums.count(secondElement) > len(nums)//3:
            result.append(secondElement)
        
        return result