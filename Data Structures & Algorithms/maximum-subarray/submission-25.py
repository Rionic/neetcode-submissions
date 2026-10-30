class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = nums[0]
        curSum = 0
        for i in range(len(nums)):
            curSum += nums[i]
            if curSum > maxSum:
                maxSum = curSum
            elif curSum < 0:
                curSum = 0

        return maxSum
