# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head: return head

        # 1 <- 2 <- 3
        #      p    c
        dummy = head
        prev = None
        while head:
            cur = head
            nxt = head.next
            cur.next = prev
            prev = cur
            head = nxt

        return prev
