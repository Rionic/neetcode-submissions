class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        sumMap = defaultdict(int)
        sumMap[0] = 1
        res, total = 0, 0

        for i in range(len(nums)):
            total += nums[i]
            if total - k in sumMap:
                res += sumMap[total - k]
            sumMap[total] += 1

        return res