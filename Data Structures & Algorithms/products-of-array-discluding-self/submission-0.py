class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        output = []
        for i, num in enumerate(nums):
            product = 1
            for j, num in enumerate(nums):
                if i!=j:
                    product *= num
            output.append(product)
        return output
