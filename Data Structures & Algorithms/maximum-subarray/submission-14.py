class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxsum = nums[0]
        cursum = 0

        for i in range(len(nums)):
            cursum += nums[i]
            if i < len(nums) - 1 and nums[i+1] > cursum + nums[i+1]:
                cursum = 0
                continue
            if cursum > maxsum:
                maxsum = cursum
            
        return maxsum

