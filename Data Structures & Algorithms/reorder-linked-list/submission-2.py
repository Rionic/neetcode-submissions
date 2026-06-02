# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        a = []
        dummy = head
        while dummy:
            a.append(dummy.val)
            dummy = dummy.next

        l, r = 0, len(a) - 1
        for i in range(len(a)):
            if i%2 == 0:
                head.val = a[l]
                l += 1
            else:
                head.val = a[r]
                r -= 1
            print(head.val)
            head = head.next
        

