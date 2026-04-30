class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        right = 0
        hashMap = {}
        longestSubstr = 0
        currLen = 0

        while left <= right and right < len(s):
            while s[right] in hashMap.keys():   
                del hashMap[s[left]]
                left += 1
            
            hashMap[s[right]] = right
            currLen = right - left + 1
            longestSubstr = max(currLen,longestSubstr)
            
            right += 1

                
        return longestSubstr