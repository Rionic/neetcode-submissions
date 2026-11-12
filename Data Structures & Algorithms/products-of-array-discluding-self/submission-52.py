class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums) 
        res = [nums[0]] * n

        for i in range(1, n):
            res[i] = res[i - 1] * nums[i]
        
        post = 1
        for i in range(n - 1, -1, -1):
            if i != 0:
                res[i] = res[i - 1] * post
            else:
                res[i] = post 
            post *= nums[i]

        return res