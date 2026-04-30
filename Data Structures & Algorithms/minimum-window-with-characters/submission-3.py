class Solution:
    def minWindow(self, s: str, t: str) -> str:
        freqMapt = {}
        freqMaps = {}
        matches = 0
        shortestSubstring = ""
        lenShortestSubstring = len(s) + 2

        left = 0
        right = 0

        for i in t:
            freqMapt[i] = freqMapt.get(i,0) + 1
        
        
        while left <= right and right < len(s):
            freqMaps[s[right]] = freqMaps.get(s[right],0) + 1

            if s[right] in freqMapt.keys() and freqMaps[s[right]] == freqMapt[s[right]]:
                matches += 1
            

            while matches == len(freqMapt):
                if right - left + 1 < lenShortestSubstring:
                    shortestSubstring = s[left:right + 1]
                    lenShortestSubstring = right - left + 1
                if s[left] in freqMapt.keys() and  freqMaps[s[left]] == freqMapt[s[left]]:
                    matches -= 1
                freqMaps[s[left]] -= 1
                left += 1

            right += 1
    
        return shortestSubstring