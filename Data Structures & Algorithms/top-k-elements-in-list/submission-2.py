import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map = defaultdict(int)
        for num in nums:
            freq_map[num]+=1
        top_freq = sorted(freq_map.items(), key=lambda kv: kv[1], reverse=True)
        top_k = [pair[0] for i, pair in enumerate(top_freq) if i < k]
        # for i, pair in enumerate(top_freq):
        #     if i < k:
        #         top_k.append(pair[0])
        return top_k
