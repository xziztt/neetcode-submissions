class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefixSum = 0
        prefixSumMap = {0:1}
        countOfLcs = 0

        for i in nums:
            prefixSum += i

            if prefixSum - k in prefixSumMap.keys():
                countOfLcs += prefixSumMap[prefixSum - k]
            
            prefixSumMap[prefixSum] = prefixSumMap.get(prefixSum, 0) + 1
        

        return countOfLcs