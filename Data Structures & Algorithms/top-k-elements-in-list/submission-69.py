class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        freqMap = defaultdict(int)

        for i in range(len(nums)):
            freqMap[nums[i]] += 1

        pairs = []
        for key, v in freqMap.items():
            pairs.append((-v, key))

        res = []

        heapq.heapify(pairs)
        while k > 0:
            res.append(heapq.heappop(pairs)[1])
            k -= 1
        
        return res
