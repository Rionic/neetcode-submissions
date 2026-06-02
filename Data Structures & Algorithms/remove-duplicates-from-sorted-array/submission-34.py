class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l, r = 1, 1

        while r < len(nums):
            if nums[r - 1] != nums[r]:
                nums[l] = nums[r]
                r += 1
                l += 1
            else:
                r += 1

        return l

# 2,10,30,10,30,30]
#         l
#                   r        