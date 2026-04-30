class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        currString = ""
        currRepetitions = 0
        for i in range(len(s)):
            if s[i].isdigit():
                currRepetitions = currRepetitions * 10 + int(s[i])
            elif s[i] == "[":
                stack.append([currString,currRepetitions])
                currString = ""
                currRepetitions = 0
            elif s[i] == "]":
                poppedElement = stack.pop()
                currString = poppedElement[0] + poppedElement[1] * currString
            else:
                currString += s[i]
        

        return currString