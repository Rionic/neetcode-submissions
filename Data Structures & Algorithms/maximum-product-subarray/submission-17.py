class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # [ 2 4 -3 5 1]
        if len(nums) == 1: return nums[0]
        maxp = max(nums)
        prod = nums[0]

        for i in range(1, len(nums)):
            if nums[i] == 0:
                prod = 1
            else:
                prod *= nums[i]
                maxp = max(maxp, prod)

        prod = nums[-1]
 
        for i in range(len(nums) -2, -1, -1):
            if nums[i] == 0:
                prod = 1
            else:
                prod *= nums[i]
                maxp = max(maxp, prod)

        return maxp

        # maxp = nums[0]
        # for i in range(len(nums)):
        #     prod = 1
        #     for j in range(i, len(nums)):
        #         prod *= nums[j]
        #         maxp = max(maxp, prod)

        # return maxp