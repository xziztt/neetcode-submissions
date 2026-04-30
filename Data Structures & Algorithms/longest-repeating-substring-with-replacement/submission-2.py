class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        right = 0
        longestSubstring = 0
        freqMap = {}
        maxFreq = 0
        while left <= right and right < len(s):
            freqMap[s[right]] = freqMap.get(s[right],0) + 1
            maxFreq = max(maxFreq, freqMap[s[right]])

            # within our n sized widow, one element will be the max

            while right-left+1 - maxFreq > k:
                freqMap[s[left]] -=1
                left +=1
        
            longestSubstring = max(longestSubstring,right-left + 1)
            right += 1    

        return longestSubstring

            