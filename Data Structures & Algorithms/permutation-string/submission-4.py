class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        left = 0
        right = 0

        matches = 0

        freqS1Map = {}
        freqS2Map = {}

        for i in s1:
            freqS1Map[i] = freqS1Map.get(i,0) + 1

        while left <= right and right < len(s2):
            freqS2Map[s2[right]] = freqS2Map.get(s2[right], 0) + 1

            while right - left + 1 > len(s1):
                
                if s2[left] in freqS1Map.keys():
                    if freqS2Map[s2[left]] == freqS1Map[s2[left]]:
                        matches -= 1
                    elif freqS2Map[s2[left]] == freqS1Map[s2[left]] + 1:
                        matches += 1
                
                freqS2Map[s2[left]] -= 1
                left += 1


            if s2[right] in freqS1Map.keys():   
                if freqS2Map[s2[right]] == freqS1Map[s2[right]]:
                    matches += 1
                elif freqS2Map[s2[right]] == freqS1Map[s2[right]] + 1:
                    matches -= 1
            
            if matches == len(freqS1Map.keys()):
                return True
            
            right += 1
        
        return False