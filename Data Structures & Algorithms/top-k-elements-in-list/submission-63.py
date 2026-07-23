class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numFreq = defaultdict(int)
        freqNum = [[] for i in range(len(nums) + 1)]

        for n in nums:
            numFreq[n] += 1
        for num, freq in numFreq.items():
            freqNum[freq].append(num)

        res = []
        for i in range(len(freqNum) - 1, -1, -1):
            for num in freqNum[i]:
                res.append(num)
                k -= 1
                if k == 0: return res