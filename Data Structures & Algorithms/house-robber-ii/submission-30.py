class Solution:
    def rob(self, nums: List[int]) -> int:
        
        def findMax(nums):
            rob1, rob2 = 0, 0
            for n in nums:
                newRob = max(n + rob2, rob1)
                rob2 = rob1
                rob1 = newRob
            return rob1

        return max(nums[0], findMax(nums[1:]), findMax(nums[:-1]))