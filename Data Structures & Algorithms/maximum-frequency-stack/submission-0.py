class FreqStack:

    def __init__(self):
        self.freqMap = {}
        self.freqGroup = {}
        self.maxFreq = 0

    def push(self, val: int) -> None:
        self.freqMap[val] = self.freqMap.get(val,0)  + 1

        if self.freqMap[val] not in self.freqGroup.keys():
            self.freqGroup[self.freqMap[val]] = [val]
        else:
            self.freqGroup[self.freqMap[val]].append(val)

        self.maxFreq = max(self.maxFreq,self.freqMap[val])
            
    def pop(self) -> int:
        toReturn = self.freqGroup[self.maxFreq].pop()
        self.freqMap[toReturn] -= 1

        if not self.freqGroup[self.maxFreq]:
            self.maxFreq-=1


        return toReturn


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()