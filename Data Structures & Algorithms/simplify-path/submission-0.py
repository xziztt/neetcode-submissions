class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []

        elements = path.split("/")
        print(elements)
        for i in elements:
            match i:
                case "..":
                    if stack:
                        stack.pop()
                case ".":
                    continue
                case "":
                    continue
                case _:
                    stack.append(i)

        print(stack)
        return "/" + "/".join(stack)
                
