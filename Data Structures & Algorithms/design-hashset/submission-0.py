class Node:
    def __init__(self, key, next=None):
        self.key = key
        self.next = next
class MyHashSet:

    def __init__(self):
        self.ListNodeValues = [Node(0) for i in range(10**4)]

    def add(self, key: int) -> None:
        toAdd = self.ListNodeValues[key % len(self.ListNodeValues)]
        while toAdd.next:
            if toAdd.next.key == key:
                return
            toAdd = toAdd.next
        toAdd.next = Node(key)

    def remove(self, key: int) -> None:
        toRemove = self.ListNodeValues[key % len(self.ListNodeValues)]
        
        while toRemove.next:
            if toRemove.next.key == key:
                toRemove.next = toRemove.next.next
                return
            toRemove = toRemove.next        

    def contains(self, key: int) -> bool:
        toContain = self.ListNodeValues[key % len(self.ListNodeValues)]

        while toContain.next:
            if toContain.next.key == key:
                return True
            toContain = toContain.next
        
        return False
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)