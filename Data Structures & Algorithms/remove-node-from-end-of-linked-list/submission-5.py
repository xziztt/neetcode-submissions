# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        slow = head

        lenList = 0
        while slow:
            lenList += 1
            slow = slow.next
        
        toRemove = lenList - n


        temp = head
        prev = None
        for i in range(0,toRemove):
            print(temp.val)
            prev = temp
            temp = temp.next
            

        if prev:
            prev.next = prev.next.next
        else:
            head = head.next
        

        return head