class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        LIS = [1] * len(nums)
        # [9,1,4,2,3,3,7]
        #        ^
        for i in range(len(nums) - 1, -1, -1):
            maxLIS = 1
            #LIS[i] = max(1 + LIS[i + 1], 1 + LIS[i + 2], 1 + LIS[i + 3]...)
            for j in range(i, len(nums)):
                if nums[j] > nums[i]:
                    maxLIS = max(maxLIS, 1 + LIS[j])
            LIS[i] = maxLIS
        print(LIS)
        return max(LIS)