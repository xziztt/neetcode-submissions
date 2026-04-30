class MinStack:

    def __init__(self):
        self.s1 = []
        self.minlist = []
    def push(self, val: int) -> None:
        self.s1.append(val)
        if len(self.minlist) == 0:
            self.minlist.append(val)
        else:
            self.minlist.append(min(self.minlist[-1], val))

    def pop(self) -> None:
        self.s1.pop()
        self.minlist.pop()

    def top(self) -> int:
         return self.s1[-1]

    def getMin(self) -> int:
        return self.minlist[-1]