# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head:
            return None

        dummy = head
        length = 0
        while head:
            length += 1
            head = head.next
        
        removeIdx = length - n

        if removeIdx == 0:
            return dummy.next
        cur, prev = dummy.next, dummy

        for i in range(1, removeIdx):
            prev = prev.next
            cur = cur.next

        prev.next = cur.next

        return dummy


        