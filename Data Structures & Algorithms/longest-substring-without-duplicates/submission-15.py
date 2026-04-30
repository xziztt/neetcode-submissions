class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        locationMap = {}
        left = 0
        right =0
        longestSubstring = 0 

        while left <= right and right < len(s):
            
            while s[right] in locationMap.keys() and left <= locationMap[s[right]]:
                del locationMap[s[left]]
                left += 1
                    
            
            longestSubstring = max(longestSubstring, right - left + 1) 
            print(right, left, right - left +1)
            locationMap[s[right]] = right

            right += 1
        
        return longestSubstring
