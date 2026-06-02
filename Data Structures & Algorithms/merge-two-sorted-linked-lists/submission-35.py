# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode()
        new = head

        while list1 and list2:

            if list1.val <= list2.val:
                new.val = list1.val
                list1 = list1.next

            else:
                new.val = list2.val
                list2 = list2.next

            new.next = ListNode()
            new = new.next
        
        if list1:
            new.val = list1.val
            new.next = list1.next
            return head

        if list2:
            new.val = list2.val
            new.next = list2.next
            return head