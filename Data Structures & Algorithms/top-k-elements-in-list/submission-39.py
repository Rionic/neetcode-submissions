class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int)

        for num in nums:
            freq[num] += 1
        
        freq_arr = [[] for _ in range(len(nums) + 1)]
        print(freq)
        for key, v in freq.items():
            freq_arr[v].append(key)
        res = []
        print(freq_arr)
        for i in range(len(freq_arr) -1, -1, -1):
            if freq_arr[i]:
                for j in range(len(freq_arr[i])):
                    print(i, freq_arr[i], k)
                    if k <= 0:
                        return res
                    res.append(freq_arr[i][j])
                    k -= 1
        return res