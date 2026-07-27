class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 2: return max(nums)
        rob = [0] * len(nums)
        rob[0] = nums[0]
        rob[1] = max(nums[0], nums[1])

        for i in range(2, len(nums)):
            rob[i] = max(rob[i - 1], rob[i - 2] + nums[i])
        print(rob)
        return max(rob[-1], rob[-2])    
            