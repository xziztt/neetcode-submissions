class HashNode:
    def __init__(self,key = -1,value = -1):
        self.key = key
        self.value = value

class MyHashMap:
    def __init__(self):
        self.hashMap = [HashNode() for i in range(10**4)]

    def put(self, key: int, value: int) -> None:
        toPut = self.hashMap[key % len(self.hashMap)]
        toPut.key = key
        toPut.value = value
        return
        

    def get(self, key: int) -> int:
        toGet = self.hashMap[key % len(self.hashMap)]
        return toGet.value

    def remove(self, key: int) -> None:
        toRemove = self.hashMap[key % len(self.hashMap)]
        toRemove.key = -1
        toRemove.value = -1

        return

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)