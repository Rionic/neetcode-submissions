class Solution:
    def rob(self, nums: List[int]) -> int:
    
        def robSub(nums):
            one, two = 0, 0
            for num in nums:
                three = max(num + one, two)
                one = two
                two = three

            return two

        return max(nums[0], robSub(nums[1:]), robSub(nums[:-1]))
