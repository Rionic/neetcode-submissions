class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]
        curMin = nums[0]
        curMax = nums[0]

        # At each point, we either have a positive or negative number, and it may be a new min or max
        # [positive] * neg -> this subarray will produce a new min
        # [negative] * pos -> this subarray will produce a new max
        # the negative case must represent the entire subarr [pos] * neg. Vice versa for pos

        for i in range(len(nums) - 1):

            maxProd = curMax * nums[i + 1] # This could be a new max, or n is negative, and its a new min!
            minProd = curMin * nums[i + 1]

            curMax = max(maxProd, minProd, nums[i + 1])
            curMin = min(maxProd, minProd, nums[i + 1])

            res = max(curMax, res)
        
        return res
