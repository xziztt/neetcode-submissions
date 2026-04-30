class TimeMap:

    def __init__(self):
        self.timeMap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.timeMap:
            self.timeMap[key] = [(value,timestamp)]
        else:
            self.timeMap[key].append((value,timestamp))

    def get(self, key: str, timestamp: int) -> str:
        
        if key not in self.timeMap:
            return ""

        mapVal = self.timeMap[key]


        left, right = 0, len(mapVal) - 1
        currVal = ""

        while left <= right:
            mid = left + (right - left)//2
            if mapVal[mid][1] <= timestamp:
                currVal = mapVal[mid][0]
                left = mid + 1
            elif mapVal[mid][1] > timestamp:
                right = mid - 1
        
        return currVal
        
