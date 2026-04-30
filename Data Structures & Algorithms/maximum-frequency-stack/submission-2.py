class FreqStack:

    def __init__(self):
        self.freqMap = {}
        self.freqStackMap = {}
        self.maxFreq = 0

    def push(self, val: int) -> None:
        self.freqMap[val] = self.freqMap.get(val,0) + 1
        if self.freqMap[val] not in self.freqStackMap.keys():
            self.freqStackMap[self.freqMap[val]] = [val]
        else:
            self.freqStackMap[self.freqMap[val]].append(val)
        self.maxFreq = max(self.maxFreq,self.freqMap[val])

    def pop(self) -> int:
        element = self.freqStackMap[self.maxFreq].pop()
        self.freqMap[element] = self.freqMap.get(element,1) - 1

        if not self.freqStackMap[self.maxFreq]:
            self.maxFreq -= 1

        return element
        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()