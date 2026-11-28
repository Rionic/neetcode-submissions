# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap, counter = [], count()
        head, tail = None, None
        for node in lists:
            if node:
                heapq.heappush(heap, (node.val, next(counter), node))


        while heap:
            val, _, node = heapq.heappop(heap)

            if not head:
                head = node
                tail = node
            else:
                tail.next = node
                tail = tail.next
            node = node.next
            if node:
                heapq.heappush(heap, (node.val, next(counter), node))

        return head