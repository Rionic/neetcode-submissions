class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        best = nums[0]
        curSum = 0

        for n in nums:
            if curSum < 0:
                curSum = 0
            curSum += n
            best = max(best, curSum)

        return best