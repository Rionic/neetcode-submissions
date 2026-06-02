class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqMap = defaultdict(int)

        for num in nums:
            freqMap[num] += 1
        
        freqArr = [ [] for i in range(len(nums) + 1)]

        for num in freqMap:
            freqArr[freqMap[num]].append(num)
        freqArr = freqArr[::-1]

        topK = []
        cur_k = 0

        for nums in freqArr:
            for num in nums:
                if len(topK) < k:
                    topK.append(num)
                else:
                    return topK
        return topK