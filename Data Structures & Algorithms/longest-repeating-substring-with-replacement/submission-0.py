class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        right = 0
        maxFrequency= 0 
        freqMap = {}
        while left <= right and right < len(s):
            freqMap[s[right]]= freqMap.get(s[right],0) + 1
            maxFrequency = max(maxFrequency,freqMap[s[right]])
            
            while (right-left + 1) - maxFrequency > k:
                freqMap[s[left]] -= 1
                left += 1
            
            right += 1
            
        
        return right-left

