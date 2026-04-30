# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        currList = ListNode(0,None)
        dummy = currList
        while list1 and list2:
            
            if list2.val > list1.val:
                currList.next = list1
                list1 = list1.next
            else:
                currList.next = list2
                list2 = list2.next
            currList = currList.next

        if list1:
            currList.next = list1
        
        if list2:
            currList.next = list2

        return dummy.next

