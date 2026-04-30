class Solution:
    def minWindow(self, s: str, t: str) -> str:
        freqS = {}
        freqT = {}

        left = 0
        right = 0
        
        lenMinSubstring = float("inf")
        minSubstring = ""

        matches = 0

        if len(s) < len(t):
            return minSubstring

        for i in t:
            freqT[i] = freqT.get(i,0) + 1

        while left <= right and right < len(s):
            freqS[s[right]] = freqS.get(s[right],0) + 1
            if s[right] in freqT.keys() and freqS[s[right]] == freqT[s[right]]:
                matches += 1
            
            while matches == len(freqT):
                if right - left + 1 < lenMinSubstring:
                    minSubstring = s[left:right + 1]
                    lenMinSubstring = len(minSubstring)
                if s[left] in freqT.keys() and freqS[s[left]] == freqT[s[left]]:
                    matches -= 1
                freqS[s[left]] -= 1
                left += 1

            right += 1

        return minSubstring