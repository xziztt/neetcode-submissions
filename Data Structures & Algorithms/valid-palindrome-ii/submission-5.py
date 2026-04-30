class Solution:
    def validPalindrome(self, s: str) -> bool:
        def isPalindrome(left,right):
            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            
            return True
        

        if len(s) in [0,1]:
            return True

        left = 0
        right = len(s) - 1

            
        while s[left] == s[right] and left < right:
            right -= 1
            left += 1

        return isPalindrome(left,right - 1) or isPalindrome(left + 1,right)
        
