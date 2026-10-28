class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        LIS = [1] * len(nums)
        for i in range(len(nums)):
            maxLIS = 1
            #LIS[i] = max(1 + LIS[i + 1], 1 + LIS[i + 2], 1 + LIS[i + 3]...)
            for j in range(i):
                if nums[j] < nums[i]:
                    maxLIS = max(maxLIS, 1 + LIS[j])
            LIS[i] = maxLIS

        return max(LIS)