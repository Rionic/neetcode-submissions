# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# [1,2,3,1]
#  s f 
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head or head.next == None:
            return False
        slow = head
        fast = head.next
        i = 0

        while fast != None:
            if slow == fast:
                return True
            i += 1
            fast = fast.next
            if i%2 == 0:
                slow = slow.next
        return False
