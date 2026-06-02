class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap = []
        for num in nums:
            heapq.heappush(self.heap, -num)
        self.k = k

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, -val)
        return -heapq.nsmallest(self.k, self.heap)[-1]

    

        
