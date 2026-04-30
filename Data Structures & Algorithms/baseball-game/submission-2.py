class Solution:
    def calPoints(self, operations: List[str]) -> int:
        opOutput = []
        val = 0
        for i in operations:
            print(opOutput)
            is_int = lambda s: s.lstrip('-').isdigit()
            if is_int(i):
                opOutput.append(int(i))
                val += opOutput[-1]
            elif i == "+":
                opOutput.append(int(opOutput[-1]) + int(opOutput[-2]))
                val += opOutput[-1]
            elif i == "D":
                opOutput.append(2 * int(opOutput[-1]))
                val -= opOutput[-1]
            elif i == "C":
                val -= opOutput[-1]
                opOutput.pop()

        val = 0    
        for i in opOutput:
            val += i
        
        return val
