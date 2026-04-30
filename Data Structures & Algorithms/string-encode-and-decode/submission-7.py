class Solution:

    def encode(self, strs: List[str]) -> str:
        encodedString  = ""
        for i in strs:
            encodedString += str(len(i)) + "#" + i
        
        return encodedString
    def decode(self, s: str) -> List[str]:
        i = 0
        j = 0
        decodedString = []
        while i < len(s):
            j = i
            while s[j] != "#":
                j+=1
            
            print(s[i:j])
            element = s[i:j]
            length = int(element)
            i = j + 1
            decodedString.append(s[i:i+length])
            i += length
            
        return decodedString