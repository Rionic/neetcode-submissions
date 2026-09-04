class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        running, count = 0, 0
        prefix = defaultdict(int)
        prefix[0] = 1
        for i in range(len(nums)):
            running += nums[i]
            count += prefix[running - k]
            prefix[running] += 1

        return count