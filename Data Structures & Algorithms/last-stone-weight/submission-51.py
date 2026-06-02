class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # stones = [6,4,3,2,2]
        # [3, 2, 2, 2]
        # [2, 2, 1]
        # [1]
        # 
        stone_heap = []

        for s in stones:
            heapq.heappush(stone_heap, -s)
        
        while stone_heap:
            largest = heapq.heappop(stone_heap)
            if stone_heap:
                s_largest = heapq.heappop(stone_heap)
                new = s_largest - largest
                if new:
                    heapq.heappush(stone_heap, -new)
                largest = 0
            print(stone_heap)
        
        return -largest 


