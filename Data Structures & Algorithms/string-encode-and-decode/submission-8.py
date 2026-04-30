class Solution:

    def encode(self, strs: List[str]) -> str:
        encodedString = ""
        for i in strs:
            encodedString += str(len(i)) + "#" + i
        return encodedString

    def decode(self, s: str) -> List[str]:
        left = 0
        right = 0
        decodedString = []
        while right < len(s):
            
            if s[right] == "#":
                length = int(s[left:right])
                right += 1
                actualString = s[right:right + length]
                decodedString.append(actualString)
                right += length
                left = right
            right += 1
        
        return decodedString