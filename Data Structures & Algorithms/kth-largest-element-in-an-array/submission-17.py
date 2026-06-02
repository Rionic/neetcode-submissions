class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []

        for num in nums:
            if len(heap) == k:
                if heap[0] < num:
                    heapq.heappop(heap)
                else:
                    continue
            heapq.heappush(heap, num)
            print(heap)
        return heapq.heappop(heap)