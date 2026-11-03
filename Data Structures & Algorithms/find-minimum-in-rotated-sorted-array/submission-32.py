class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        min_num = 0

        while l < r:
            m = (l + r) // 2
            if nums[m] > nums[r]: # Answers in this half
                min_num = min(min_num, nums[r])
                l = m + 1
            else:
                min_num = min(min_num, nums[m], nums[l])
                r = m

        return nums[r]