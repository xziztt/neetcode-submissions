class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        elementFreq = {}
        for i in nums:
            elementFreq[i] = elementFreq.get(i,0) + 1
        
        sortedFrequent = sorted(elementFreq.items(),key=lambda item: item[1], reverse=True)
        print(sortedFrequent)
        topKFrequent = []
        i = 0
        while k > 0 and i < len(sortedFrequent):

            if sortedFrequent[i][0] not in topKFrequent:
                topKFrequent.append(sortedFrequent[i][0])
                k-=1
            i+=1
        return topKFrequent