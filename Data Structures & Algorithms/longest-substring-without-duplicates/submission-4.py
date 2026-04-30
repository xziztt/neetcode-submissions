class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seenElements = {}
        maxLen = 0
        left = 0
        right = 0
        while left <= right and right < len(s):
            while s[right] in seenElements.keys():
                seenElements.pop(s[left])
                left += 1

            maxLen = max(maxLen, right - left + 1)
            seenElements[s[right]] = right
            right += 1
        
        return maxLen