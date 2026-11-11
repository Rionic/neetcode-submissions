class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxp = nums[0]
        minp = nums[0]
        res = nums[0]
        # [-3,1,-4,1,-2,10]
        for num in nums[1:]:
            # if num == 0:
            #     minp, maxp = 1, 1
            #     continue
            a = minp * num
            b = maxp * num
            maxp = max(a, b, num)
            minp = min(a, b, num) 
            res = max(res, maxp)
        return res