class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numsSet = set()
        for i in nums:
            numsSet.add(i)
        
        currLen = 0
        longestLen = 0
        for i in nums:
            currElement = i
            currLen = 0
            while True:
                if currElement in numsSet:
                    currLen += 1
                    longestLen = max(longestLen,currLen)
                    currElement -= 1
                    continue
                else:
                    break
        return longestLen
