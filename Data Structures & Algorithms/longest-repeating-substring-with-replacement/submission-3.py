class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        freqMap = {}
        right = 0
        maxFreq = 0
        longestSubstring = 0

        while left <= right and right < len(s):
            freqMap[s[right]] = freqMap.get(s[right],0) + 1
            maxFreq = max(maxFreq,freqMap[s[right]])

            while  k < right - left + 1 - maxFreq:
                freqMap[s[left]] -= 1
                left += 1
            

            longestSubstring = max(longestSubstring, right-left + 1)
            right += 1
    
        return longestSubstring


