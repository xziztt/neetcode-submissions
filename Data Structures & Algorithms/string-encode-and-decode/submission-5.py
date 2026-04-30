class Solution:

    def encode(self, strs: List[str]) -> str:
        encodedString = ""

        
        for i in range(0,len(strs)):           
            encodedString += strs[i]
            encodedString += "||"
        
        return encodedString

    def decode(self, s: str) -> List[str]:
        if len(s) == 0:
            return []
        decodedString = s.split("||")
        return decodedString[0:len(decodedString) - 1]
