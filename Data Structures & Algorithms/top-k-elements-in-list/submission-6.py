import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map = defaultdict(int)

        for num in nums:
            freq_map[num]+=1

        freq_arr = [[] for _ in range(max(freq_map.values()) + 1)]

        for kv in freq_map.items():
            freq_arr[kv[1]].append(kv[0])

        freq_arr = freq_arr[::-1]
        top_k = []

        for nums in freq_arr:
            if len(nums) == 0:
                continue
            for num in nums:
                top_k.append(num)
                if len(top_k) == k:
                    return top_k
        
