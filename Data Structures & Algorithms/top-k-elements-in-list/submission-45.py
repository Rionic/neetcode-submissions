class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqMap = defaultdict(int)

        for i, n in enumerate(nums):
            freqMap[n] += 1
        heap = []

        for key in freqMap:
            heapq.heappush(heap, (-freqMap[key], key))

        res = []
        while k:
            res.append(heapq.heappop(heap)[1])
            k -= 1
        return res