class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0: return 0
        if len(nums) == 1: return nums[0]

        maxArr = [0] * len(nums)
        maxArr[0] = nums[0]
        maxArr[1] = max(nums[0], nums[1])

        for i in range(2, len(nums)):
            maxArr[i] = max(nums[i] + maxArr[i - 2],
                            maxArr[i - 1])
            
        return max(maxArr[-1], maxArr[-2])
            
