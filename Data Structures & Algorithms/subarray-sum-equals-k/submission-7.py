class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefixSums = defaultdict(int)
        prefixSums[0] = 1
        total = 0
        res = 0
        # [1 3 2 3 8]
        # [1 4 6 9 17]
        #  total - k 
        # 13
        # [-1 -1 1]
        # [-1 -2 -1]
        #      
        # 0
        for i in range(len(nums)):
            total += nums[i]
            if total - k in prefixSums:
                res += prefixSums[total - k]
            prefixSums[total] += 1

        print(prefixSums)
        return res