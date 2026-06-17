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
        cur, prev = dummy, None

        if removeIdx == 0:
            return dummy.next

        for i in range(removeIdx):
            if i == 0:
                prev = dummy
            else:
                prev = prev.next
            cur = cur.next

        if prev is None: # Removing first element
            dummy = dummy.next
        else:
            prev.next = cur.next

        return dummy


        