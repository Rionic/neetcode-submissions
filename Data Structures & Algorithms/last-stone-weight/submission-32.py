class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []
        for stone in stones:
            heapq.heappush(heap, -stone)
        print(heap)
        while len(heap) > 1:
            s1 = heapq.heappop(heap)
            s2 = heapq.heappop(heap)
            if abs(s2) > abs(s1):
                s2 -= s1
                s1 = 0
            elif abs(s1) > abs(s2):
                s1 -= s2
                s2 = 0
            else:
                s1, s2 = 0, 0
            if s1 != 0:
                heapq.heappush(heap, s1)
            if s2 != 0:
                heapq.heappush(heap, s2)
            print(heap)
        if heap:
            return abs(heap[0])
        return 0