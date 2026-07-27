class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 2: return max(nums)
        one, two = nums[0], max(nums[0], nums[1])

        for i in range(2, len(nums)):
            one, two = two, max(two, nums[i] + one)

        return two 
            