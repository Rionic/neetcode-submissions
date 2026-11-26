class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        buckets = [[] for _ in range(len(nums) + 1)]

        for num, count in freq.items():
            buckets[count].append(num)

        res = []

        for i in range(len(buckets) -1, -1, -1):
            length = len(buckets[i])
            while length > 0 and k > 0:
                res.append(buckets[i].pop())
                length = len(buckets[i])
                k -= 1
    
        return res