class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for i in s:
            if i in ["{","(","["]:
                stack.append(i)
            else:
                if len(stack) == 0:
                    return False
                if i == "}" and stack[-1] != "{":
                        return False
                elif i == ")" and stack[-1] != "(":
                    return False
                elif i == "]" and stack[-1] != "[":
                    return False

                stack.pop()
        
        return len(stack) == 0