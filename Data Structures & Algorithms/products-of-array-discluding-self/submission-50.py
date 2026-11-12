class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre, post = [nums[0]] * len(nums), [nums[-1]] * len(nums)

        for i in range(1, len(nums)):
            pre[i] = pre[i - 1] * nums[i]

        for i in range(len(nums) - 2, -1, -1):
            post[i] = post[i + 1] * nums[i]

        res = []
        for i in range(len(nums)):
            prod = 1
            if i > 0:
                prod *= pre[i - 1]
            if i < len(nums) - 1:
                prod *= post[i + 1] 
            res.append(prod)

        return res