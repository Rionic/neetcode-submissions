class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0: return 0
        if len(nums) == 1: return nums[0]
    
        def robSub(nums):
            one, two = 0, 0
            for num in nums:
                three = max(num + one, two)
                one = two
                two = three

            return two

        return max(robSub(nums[1:]), robSub(nums[:-1]))
