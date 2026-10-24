class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Array of len 1000. index represents frequency, value are the nums with that frequency

        freqMap = Counter(nums)
        freqArr = [[] for n in range(len(nums) + 1)]

        for num, freq in freqMap.items():
            freqArr[freq].append(num)

        res = []

        for bucket in reversed(freqArr):
            res.extend(bucket)

            if len(res) >= k:
                return res[:k]
