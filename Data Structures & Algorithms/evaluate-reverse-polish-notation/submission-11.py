class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for i in tokens:
            match i:
                case "*":
                    elementOne = stack.pop()
                    elementTwo = stack.pop()

                    stack.append(elementTwo * elementOne)
                case "/":
                    elementOne = stack.pop()
                    elementTwo = stack.pop()
                    val = int(elementTwo/elementOne)

                    stack.append(val)
                    
                case "+":
                    elementOne = stack.pop()
                    elementTwo = stack.pop()

                    stack.append(elementTwo + elementOne)
                case "-":
                    elementOne = stack.pop()
                    elementTwo = stack.pop()

                    stack.append(elementTwo - elementOne)
                case _:
                    stack.append(int(i))
            print(stack)

        return stack[0]

