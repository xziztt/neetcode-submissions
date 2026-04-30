class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        buckets = [[] for i in range(0,len(nums))]

        frequencyMap = {}
        for i in nums:
            frequencyMap[i] = frequencyMap.get(i,0) + 1
        
        freqMapLen = len(frequencyMap)
        
        print(frequencyMap)
        print(buckets)

        for i in frequencyMap.keys():
            buckets[frequencyMap[i] - 1].append(i)
            print(buckets)
        
        finalList = []

        print(frequencyMap)
        print(buckets)

        for i in range(len(buckets) - 1,-1,-1):
            for j in range(0,len(buckets[i])):
                if k > 0:
                    finalList.append(buckets[i][j])
                    k-=1
        
        return finalList
