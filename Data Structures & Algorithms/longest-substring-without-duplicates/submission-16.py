class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        right = 0
        foundMap = {}
        maxLength = 0

        while left <= right and right < len(s):
            if s[right] in foundMap.keys():
                while s[right] in foundMap.keys():
                    del foundMap[s[left]]
                    left += 1
                
            maxLength = max(maxLength, right-left + 1)
            foundMap[s[right]] = right
            right += 1
                

        return maxLength