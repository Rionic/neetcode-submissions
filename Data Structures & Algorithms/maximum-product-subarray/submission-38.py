class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]
        maxNeg = nums[0]
        maxPos = nums[0]

        for i in range(len(nums) - 1):
            
            a = nums[i + 1] * maxNeg
            b = nums[i + 1] * maxPos

            maxNeg = min(a, b, nums[i + 1])
            maxPos = max(a, b, nums[i + 1])
            res = max(res, maxPos)
        
        return res
