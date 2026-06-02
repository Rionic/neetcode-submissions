class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []
        for stone in stones:
            heapq.heappush(heap, -stone)

        while len(heap) > 1:
            s1 = heapq.heappop(heap)
            s2 = heapq.heappop(heap)
            if s1 < s2: # This is always true due to the heap property
                heapq.heappush(heap, s1 - s2)
        if heap:
            return abs(heap[0])
        return 0