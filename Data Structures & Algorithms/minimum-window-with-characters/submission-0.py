class Solution:
    def minWindow(self, s: str, t: str) -> str:
        left = 0
        right = 0
        matches = 0
        freqMapS = {}
        freqMapT = {}
        minLength = float("inf")
        minWindow = ""

        if len(t) > len(s):
            return ""

        for i in t:
            freqMapT[i] = freqMapT.get(i,0) + 1

        while left <= right and right < len(s):
                
            freqMapS[s[right]] = freqMapS.get(s[right],0) + 1
            if s[right] in freqMapT.keys() and freqMapS[s[right]] == freqMapT[s[right]]:
                matches += 1

            while matches == len(freqMapT):
                if right - left + 1 < minLength:
                    minLength = right-left + 1
                    minWindow = s[left:right+1]
 
                if s[left] in freqMapT.keys() and freqMapS[s[left]] == freqMapT[s[left]]:
                    matches -= 1
                
                freqMapS[s[left]] -=1
                left += 1

            right += 1

        
        return minWindow