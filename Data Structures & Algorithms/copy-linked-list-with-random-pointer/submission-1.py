"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        curr = head
        prev = None
        hashMap = {}

        if not head:
            return head

        while curr:
            newNode = Node(curr.val, curr.next, curr.random)
            hashMap[curr] = newNode
            curr = curr.next
        
        curr = head

        while curr:
            copyNode = hashMap[curr]
            copyNode.next = hashMap[curr.next] if curr.next else None
            copyNode.random = hashMap[curr.random] if curr.random else None
            curr = curr.next
        

        return hashMap[head]