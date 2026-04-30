class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefixSum = 0
        freqMap = {0:1}
        countOfOccurance = 0

        for i in nums:
            prefixSum += i

            if prefixSum - k in freqMap.keys():
                 countOfOccurance += freqMap[prefixSum - k]
            


            freqMap[prefixSum] = freqMap.get(prefixSum,0) + 1
        

        return countOfOccurance