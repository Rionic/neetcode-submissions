# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap, res, counter = [], [], count()
        for head in lists:
            if head:
                heapq.heappush(heap, (head.val, next(counter), head))

        res_head, tail = None, None

        while heap:
            val, _, node = heapq.heappop(heap)

            if not res_head:
                res_head = node
                tail = node
            else:
                tail.next = node
                tail = tail.next
            
            if node.next:
                heapq.heappush(heap, (node.next.val, next(counter), node.next))

        return res_head