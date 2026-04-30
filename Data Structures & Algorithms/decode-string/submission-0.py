class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        currString = ""
        num = 0


        for i in s:
            if i.isdigit():
                num = num * 10 + int(i)
            elif i == "[":
                stack.append((currString,num))
                currString = ""
                num = 0
            elif i == "]":
                strvalue, repeat = stack.pop()
                currString = strvalue + repeat * currString
            else:
                currString += i
        
        return currString
            