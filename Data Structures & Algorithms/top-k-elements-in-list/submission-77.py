class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Array of len 1000. index represents frequency, value are the nums with that frequency

        freqMap = defaultdict(int)
        freqArr = [[] for n in range(len(nums) + 1)]

        for n in nums:
            freqMap[n] += 1

        for num, freq in freqMap.items():
            freqArr[freq].append(num)

        res = []

        for i in range(len(freqArr) - 1, -1, -1):
            for num in freqArr[i]:
                if k < 1: break
                res.append(num)
                k -= 1

        return res
