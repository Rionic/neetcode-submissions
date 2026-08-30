class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = []
        postfix = [0] * len(nums)
        product = 1
        for num in nums:
            product *= num
            prefix.append(product)
        
        product = 1
        for i in range(len(nums) - 1, - 1, - 1):
            product *= nums[i]
            postfix[i] = product
        
        product = [0] * len(nums)
        product[0] = postfix[1]
        product[-1] = prefix[-2]
        for i in range(1, len(nums) - 1):
            product[i] = prefix[i - 1] * postfix[i + 1]

        return product

        