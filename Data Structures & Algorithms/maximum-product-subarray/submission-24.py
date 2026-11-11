class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        best = max(nums)

        for arr in (nums, nums[::-1]):
            prod = 1
            for x in arr:
                if x == 0:
                    prod = 1
                else:
                    prod *= x
                    best = max(best, prod)

        return best

        # maxp = nums[0]
        # for i in range(len(nums)):
        #     prod = 1
        #     for j in range(i, len(nums)):
        #         prod *= nums[j]
        #         maxp = max(maxp, prod)

        # return maxp