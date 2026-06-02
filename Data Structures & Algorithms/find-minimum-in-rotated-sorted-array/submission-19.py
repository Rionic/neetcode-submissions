class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        res = nums[0]
        # [6, 7, 1, 2, 3, 4, 5]
        while l <= r:
            if nums[l] < nums[r]: # We are either at the smallest, or the end of alg
                return min(res, nums[l])
            m = (l + r)//2
            if nums[m] >= nums[l]: # Answer is to the right!
                l = m + 1
            else: # Answer is to the left!
                r = m - 1
            res = min(nums[m], res)

        return res