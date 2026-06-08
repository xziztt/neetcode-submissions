# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head

        while slow and fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        
        # now slow is at the middle

        prev = None
        curr = slow.next
        slow.next = None

        
        while curr:
            temp = curr.next
            curr.next = prev 
            prev = curr
            curr = temp
        
        
        left = head
        while prev and left:
            temp1, temp2 = prev.next, left.next
            left.next = prev
            prev.next = temp2
            left = temp2
            prev = temp1
                

